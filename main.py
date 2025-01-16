import os
import boto3
from botocore.exceptions import ClientError
from botocore.config import Config
import glob
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload files to AWS S3")
    parser.add_argument('--endpoint_url', required=True, help='AWS S3 bucket name')
    parser.add_argument('--key_id', required=True, help='AWS access key ID')
    parser.add_argument('--application_key', required=True, help='AWS secret access key')
    parser.add_argument('--file', required=True, help='File pattern to upload')
    parser.add_argument('--destination', required=True, help='Destination directory in bucket')
    parser.add_argument('--bucket', required=True, help='Destination bucket name')
    args = parser.parse_args()

    b2 = boto3.client(service_name='s3',
                      endpoint_url=args.endpoint_url,                # Backblaze endpoint
                      aws_access_key_id=args.key_id,              # Backblaze keyID
                      aws_secret_access_key=args.application_key, # Backblaze applicationKey
                      config=Config(signature_version='s3v4'))

    for file in glob.glob(args.file):
        try:
            response = b2.upload_file( file, args.bucket, f"{args.destination}/{os.path.basename(file)}")
            print(f'Successfully uploaded {file} to {args.destination}/{os.path.basename(file)}')
        except ClientError as e:
            print(f'Failed to upload {file}: {e}')
