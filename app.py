import boto3
import os
import pdfkit
 
# Set up the AWS credentials
access_key = '<aws-access-key>'
secret_key = '<aws-secret-key>'
 
# Set up the S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)
 
# Set up the S3 bucket and file keys
source_bucket_name = '<src-bucket-name>'
source_file_key = 'index.html'
destination_bucket_name = <destination-bucket-name>
destination_file_key = 'index.pdf'
 
# Download the HTML file from S3
response = s3.get_object(Bucket=source_bucket_name, Key=source_file_key)
html_data = response['Body'].read().decode('utf-8')
 
# Convert HTML to PDF using pdfkit
pdfkit.from_string(html_data, destination_file_key)
 
# Upload the PDF file to S3
with open(destination_file_key, 'rb') as f:
    s3.upload_fileobj(f, destination_bucket_name, destination_file_key)
