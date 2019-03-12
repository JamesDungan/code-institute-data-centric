import boto3
from botocore.exceptions import BotoCoreError
import os

ACCESS_ID = os.environ.get('ACCESS_ID')
ACCESS_KEY = os.environ.get('ACCESS_KEY')

s3 = boto3.resource('s3',
    aws_access_key_id=ACCESS_ID,
    aws_secret_access_key= ACCESS_KEY)

def upload_file(filename, file):
    try:
        response = s3.Bucket('ci-data-centric-images').put_object(Key=filename, Body=file, ACL='public-read')
    except BotoCoreError as e:
        return e
    return response

def delete_file(key):
    delete = {
        'Objects':[
            {
                'Key': key
            },
        ],
    }
    try:
        response = s3.Bucket('ci-data-centric-images').delete_objects(Delete=delete)
    except BotoCoreError as e:
        return e
    return response
