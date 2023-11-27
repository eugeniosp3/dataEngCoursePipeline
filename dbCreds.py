# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError
from config import accessKeys
from ast import literal_eval


access_key_id, secret_access_key = accessKeys()


def get_secret():

    secret_name = "data-eng-course-RDS"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key

    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    return secret
    # Your code goes here.


# string of our dictionary of credentials
db_creds = get_secret()
# evaluated the string literally to get a dictionary we can access via key value pairs
db_creds = literal_eval(db_creds)

USERNAME = db_creds['username']
PASSWORD = db_creds['password']
HOST = db_creds['host']
DATABASE = db_creds['databasename']
PORT = db_creds['port']
