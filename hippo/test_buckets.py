import boto3
import boto3.session
# from botocore.exceptions import ClientError


def main():
    session = boto3.session.Session()
    s3client = session.client(
        's3',
        use_ssl=False,
        endpoint_url='http://192.168.99.100:8080',
        aws_access_key_id='UEF4ZL22-B2YKBJ0QZBL',
        aws_secret_access_key='vImVW0uuw0e4NmWFV6UMrVX6b0dzDERx3FuTYA==')

    paginator = s3client.get_paginator('list_objects')
    result = paginator.paginate(
        Bucket='52138c33-4043-4a85-a23c-9ec9d4fd48f1',
        Delimiter='/')

    for prefix in result.search('CommonPrefixes'):
        print(prefix)


if __name__ == '__main__':
    main()
