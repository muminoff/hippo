import boto3
import boto3.session
from botocore.exceptions import ClientError


def main():
    session = boto3.session.Session()
    s3client = session.client(
        's3',
        endpoint_url='http://192.168.99.100:8080')

    # response = s3client.list_objects(Bucket='d826d38d2c7442dcb6ddd49f43491e7e')
    # print(response['Contents'])

    # response = s3client.get_bucket_location(Bucket='d826d38d2c7442dcb6ddd49f43491e7e')
    # print(response)

if __name__ == '__main__':
    main()
