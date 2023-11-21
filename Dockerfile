FROM python:3.11

# Install the AWS CLI, unzip, and any other necessary dependencies
RUN apt-get update && apt-get install -y curl unzip zip && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install

RUN pip install boto3

WORKDIR /Documenting-batch-processing/
COPY fetch.py .
CMD ["python", "fetch.py"]