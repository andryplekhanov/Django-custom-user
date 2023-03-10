# Generated by Django 4.1.7 on 2023-03-02 09:15

import app_users.validators
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyGroups',
            fields=[
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, db_index=True, max_length=20, validators=[django.core.validators.RegexValidator(message="The phone number must be specified in the following format: '+79012345678'.", regex='^\\+\\d{11,20}')], verbose_name='phone number'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'], message='Download error: Only files with the following extensions are allowed: .jpg .jpeg .png'), app_users.validators.file_size_validate], verbose_name='profile image'),
        ),
    ]
