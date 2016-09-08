# Django
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.template import defaultfilters

# Choices
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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    service = models.ForeignKey('Service', default=1)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
