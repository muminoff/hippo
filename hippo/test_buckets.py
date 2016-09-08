import boto3
import boto3.session
from botocore.exceptions import ClientError


def main():
    session = boto3.session.Session()
    s3client = session.client(
        's3',
        endpoint_url='http://192.168.99.100:8080')

    try:
        response = s3client.list_buckets()
    except ClientError as e:
        print(str(e))

    for bucket in response['Buckets']:
        print(bucket['Name'], bucket['CreationDate'])


if __name__ == '__main__':
    main()
