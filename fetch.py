
import boto3
import os

comprehend = boto3.client('comprehend')
s3 = boto3.client('s3')

    
def fetch_documents_from_s3(bucket_name, file=''):

    response = s3.get_object(Bucket=bucket_name, Key=file)
    text = response['Body'].read().decode('utf-8')
    return text
    
def remove_pii(text):
    response = comprehend.detect_pii_entities(
        Text=text,
        LanguageCode='en'
    )
    pii_entities = response['Entities']
    redacted_text = text
    for entity in pii_entities:
        start_offset = entity['BeginOffset']
        end_offset = entity['EndOffset']
        redacted_text = redacted_text[:start_offset] + "[REDACTED]" + redacted_text[end_offset:]
    return redacted_text

bucket_name = os.environ.get('BUCKET_NAME')
file = os.environ.get('FILE_NAME')


document_text = fetch_documents_from_s3(bucket_name, file)
filtered_text = remove_pii(document_text)
s3.put_object(Bucket = bucket_name, Key = file, Body = filtered_text)
print(filtered_text)