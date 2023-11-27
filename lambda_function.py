import numpy as np
import json
import time
import datetime
import boto3

from utility import generate_iot_data
from config import BUCKET_NAME
from keys import accessKeys, secretKey


# get current date and time
current_time = time.time()
# current date
current_date = time.strftime("%Y-%m-%d", time.localtime(current_time))

# build an s3 resource to put files in an s3 bucket
s3 = boto3.resource('s3',
                    aws_acc=accessKeys,
                    aws_secret_access_key=secretKey,
                    )


# create a script where every 100 records the data is reset and a new batch is created
HOURS_OF_RECORDS = 24


# create a new batch of data for the specific number of records created in the 24 hours
# why did I add 1 to the range?
# because range(0, 24) will only give me 23 hours of data, the last hour will be missing
# because range is not inclusive of the last number, so I added 1 to the range to make it inclusive of the last number
for i in range(HOURS_OF_RECORDS + 1):
    hour_log = i
    file_name = f"simulatedLog_{current_time}_{current_date}_{hour_log}.json"
    generated_data = generate_iot_data()
    # convert this dictionary into a json object
    print(generated_data)
    json_data = json.dumps(generated_data)
    # put the file into the bucket with the name of the file and the json data as the body of the file
    s3.Object(BUCKET_NAME, file_name).put(Body=json_data)
