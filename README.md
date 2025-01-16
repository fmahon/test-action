# Python S3 Upload Action

This GitHub Action uploads files to an S3-compatible bucket using Python.

## Inputs

- `endpoint_url`: URL of the S3-compatible endpoint (required)
- `key_id`: AWS access key ID (required)
- `application_key`: AWS secret access key (required)
- `file`: File pattern to upload (required)
- `destination`: Destination directory in bucket (required)
- `bucket`: Destination bucket name (required)

## Example Usage

```yaml
name: Upload to S3

on: [push]

jobs:
  upload:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Upload files to S3
        uses: ./
        with:
          endpoint_url: ${{ secrets.S3_ENDPOINT_URL }}
          key_id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          application_key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          file: 'path/to/your/file'
          destination: 'your/destination/directory'
          bucket: 'your-bucket-name'