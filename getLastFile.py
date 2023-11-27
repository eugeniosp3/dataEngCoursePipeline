import boto3
import pandas as pd
from io import StringIO
from keys import accessKey, secretKey
from config import BUCKET_NAME

# AWS S3 credentials and bucket details


def getCurrentFile(bucketName, folderName):
    """
    This function will get the current file from the S3 bucket
    Returns a Pandas DataFrame of the file content

    """
    BUCKET_NAME = bucketName
    folder_name = folderName

    # Create a boto3 client
    s3_client = boto3.client('s3', aws_access_key_id=accessKey,
                             aws_secret_access_key=secretKey)

    # Get the list of files in the folder
    objects = s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix=folder_name)

    # Find the latest file
    latest_file = None
    last_modified = None

    for obj in objects.get('Contents', []):
        if last_modified is None or obj['LastModified'] > last_modified:
            latest_file = obj['Key']
            last_modified = obj['LastModified']

    # Check if a file was found
    if latest_file is not None:
        # Download the latest file content
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key=latest_file)
        content = response['Body'].read().decode('utf-8')

        # Read the content into a Pandas DataFrame
        # Adjust the read function based on your file format (e.g., read_csv, read_excel)
        df = pd.read_csv(StringIO(content))

        # Print DataFrame (or perform other operations)
        return df
    else:
        print("No files found in the specified folder.")
