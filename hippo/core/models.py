# Django
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.template import defaultfilters
from django.conf import settings

# Boto3
import boto3
import boto3.session
from botocore.exceptions import ClientError

# Misc
import uuid


# Storage choices
STORAGE_SPACE_CHOICES = (
    (536870912, '512mb'),
    (1073741824, '1gb'),
    (2147483648, '2gb'),
    (3221225472, '3gb'),
    (4294967296, '4gb'),
    (5368709120, '5gb'),
    (10737418240, '10gb'),
)


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    space = models.BigIntegerField(choices=STORAGE_SPACE_CHOICES, default=536870912) # noqa

    def __str__(self):
        return "{} ({})".format(
            self.name, defaultfilters.filesizeformat(self.space))


class S3Account(models.Model):
    id = models.TextField(primary_key=True)
    key_id = models.TextField()
    key_secret = models.TextField()
    status = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_s3_account(sender, instance, created, **kwargs):

        if created:
            import requests
            import json
            url = settings.BACKEND_ENDPOINT_URL + '/riak-cs/user'
            data = {'email': instance.email, 'name': instance.get_full_name()}
            response = requests.post(url, json=data)
            response_dict = json.loads(response.text)
            S3Account.objects.create(
                user=instance,
                id=response_dict['id'],
                key_id=response_dict['key_id'],
                key_secret=response_dict['key_secret'],
                status=response_dict['status'])

            session = boto3.session.Session()
            s3client = session.client(
                's3',
                use_ssl=False,
                endpoint_url=settings.BACKEND_ENDPOINT_URL,
                aws_access_key_id=response_dict['key_id'],
                aws_secret_access_key=response_dict['key_secret'])

            try:
                s3client.create_bucket(Bucket=str(uuid.uuid4()))
            except ClientError as e:
                print(str(e))
                pass

    def get_buckets(self):
        session = boto3.session.Session()
        s3client = session.client(
            's3',
            use_ssl=False,
            endpoint_url=settings.BACKEND_ENDPOINT_URL,
            aws_access_key_id=self.key_id,
            aws_secret_access_key=self.key_secret)

        response = s3client.list_buckets()
        return [bucket['Name'] for bucket in response['Buckets']]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    service = models.ForeignKey('Service', default=1)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):

        if created:
            # Create default profile with default service plan
            Profile.objects.create(user=instance)
