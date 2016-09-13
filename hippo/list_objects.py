from boto3 import resource
from botocore.client import Config


def main():
    s3 = resource(
            's3',
            endpoint_url='http://localhost:9000',
            aws_access_key_id='hippohippo',
            aws_secret_access_key='hippohippo',
            config=Config(signature_version='s3v4'),
            region_name='us-east-1')
    bucket = s3.Bucket('sardor')

    result = bucket.meta.client.list_objects(
            Bucket=bucket.name,
            Delimiter='/',
            Prefix='')

    # print(result)

    isdir = 'CommonPrefixes' in result
    isfile = 'Contents' in result

    if isdir:
        for o in result.get('CommonPrefixes'):
            dirname = o.get('Prefix')
            if dirname.endswith('/') and len(dirname.split('/')) == 2:
                dirname = dirname[:-1]
            else:
                dirname = dirname.split('/')[1]

            print('❒', dirname)

    if isfile:
        for o in result.get('Contents'):
            print('☐', o.get('Key').split('/')[-1])


if __name__ == '__main__':
    main()
