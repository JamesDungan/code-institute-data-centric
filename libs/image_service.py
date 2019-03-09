import boto3
import os
from dotenv import load_dotenv

dotenv_path = 'C:\\Users\\james\\DEV\\CodeInstitute\\code-institute-data-centric\\.env'
load_dotenv(dotenv_path)

ACCESS_ID = os.environ.get('ACCESS_ID')
ACCESS_KEY = os.environ.get('ACCESS_KEY')

s3 = boto3.resource('s3',
    aws_access_key_id=ACCESS_ID,
    aws_secret_access_key= ACCESS_KEY)

def upload_file(filename, file):
    response = s3.Bucket('ci-data-centric-images').put_object(Key=filename, Body=file)
    return response
        
