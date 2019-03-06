import boto3

s3 = boto3.resource('s3')

def upload_file(filename, file):
    s3.Bucket('ci-data-centric-images').put_object(Key=filename, Body=file)
        
