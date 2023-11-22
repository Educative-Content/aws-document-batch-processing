import boto3
import os

def fetch_documents_from_s3(bucket_name, file=''):
    # Create an S3 client
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=file)
    text = response['Body'].read().decode('utf-8')

    return text

bucket_name = 'new-test-adeel'
file = os.environ.get('FILE_NAME')

document_text = fetch_documents_from_s3(bucket_name, file)
print(document_text)