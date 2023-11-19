# this script will allow us to authenticate into AWS so we can access whatever we need with the boto3 library
import pandas as pd


def accessKeys():
    """
    returns the aws access key and secret access key
    input : none
    file read: ginomain_accessKeys.csv - AWS provided access keys from IAM console

    """
    df = pd.read_csv("ginomain_accessKeys.csv")

    access_key = "Access key ID"
    secret_akey = "Secret access key"

    access_key_id = df[access_key][0]
    secret_access_key = df[secret_akey][0]
    return access_key_id, secret_access_key


BUCKET_NAME = "dataengineeringcoursebucket"
REGION = "us-east-1"
