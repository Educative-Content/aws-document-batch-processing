import boto3

def fetch_documents_from_s3(bucket_name, prefix='', file_extension=''):
  
    # Create an S3 client
    s3 = boto3.client('s3')

    # List objects in the bucket with the specified prefix and file extension
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    # Extract document information from the response
    documents = []
    for obj in response.get('Contents', []):
        key = obj['Key']
        if file_extension and not key.endswith(file_extension):
            continue  # Skip files with incorrect file extension
        documents.append({
            'Key': key,
            'Size': obj['Size'],
            'LastModified': obj['LastModified'],
        })

    return documents

# Example usage:
bucket_name = 'batch-bucket-adeel'
file_extension = '.txt'

documents = fetch_documents_from_s3(bucket_name, file_extension)
for doc in documents:
    print(f"Document Key: {doc['Key']}, Size: {doc['Size']} bytes, Last Modified: {doc['LastModified']}")
