# Generated by Django 4.2.10 on 2024-02-07 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_user_email_user_first_name_user_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
    ]
