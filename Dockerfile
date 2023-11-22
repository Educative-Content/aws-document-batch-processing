FROM python:3.11

# Install the AWS CLI, unzip, and any other necessary dependencies
RUN apt-get update && apt-get install -y curl unzip zip

RUN pip install boto3

WORKDIR /Documenting-batch-processing/
COPY fetch.py .
CMD ["python", "fetch.py"]