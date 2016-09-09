# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-09 07:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='S3Account',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('key_id', models.TextField()),
                ('key_secret', models.TextField()),
                ('status', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('space', models.BigIntegerField(choices=[(536870912, '512mb'), (1073741824, '1gb'), (2147483648, '2gb'), (3221225472, '3gb'), (4294967296, '4gb'), (5368709120, '5gb'), (10737418240, '10gb')], default=536870912)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Service'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
