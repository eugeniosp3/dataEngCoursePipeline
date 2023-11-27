import boto3
import pandas as pd
from config import accessKeys
import io
from dbWriter import writeDataToDB, testDatabaseConnection
from queryConfig import deviceInfoQuery, readingStoreQuery

access_key_id, secret_access_key = accessKeys()

# reading all files from an s3 bucket and creating a dataframe
# all files are in parquet format

s3 = boto3.client('s3',
                  aws_access_key_id=access_key_id,
                  aws_secret_access_key=secret_access_key
                  )

BUCKET = 'dataengineeringcoursebucket'
FOLDERNAME = 'hourly-logs-delta-lake/dev/'

# list all files in the folder of this bucket
files = s3.list_objects_v2(Bucket=BUCKET, Prefix=FOLDERNAME)

# get only the ones that are parquet format - the logs file will also appear here as a list of its contents
# the contents will be a series of .json files
parquetOnly = [file['Key']
               for file in files['Contents'] if file['Key'].endswith('.parquet')]


# read parquet files from parquetOnly, they are stored in s3 and must use io - just create a list of each df reading each file
def readParquetFiles(parquetOnly):
    dfList = []
    for file in parquetOnly:
        obj = s3.get_object(Bucket=BUCKET, Key=file)
        df = pd.read_parquet(io.BytesIO(obj['Body'].read()))
        dfList.append(df)
    return dfList


# can this be done as a list comprehension? YES

dfList = readParquetFiles(parquetOnly)

#  unpack deviceInfoQuery and readingStoreQuery

# convert the dataframe into a dictionary {"columnName" : value}
for dataframe in dfList:
    convertParquetToJSON = dataframe.to_dict(orient='records')
    if testDatabaseConnection():
        for row in convertParquetToJSON:
            writeDataToDB(row, deviceInfoQuery)
            writeDataToDB(row, readingStoreQuery)
    else:
        print("Database connection failed")
