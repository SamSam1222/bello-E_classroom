# Generated by Django 4.2.10 on 2024-02-07 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0009_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='user_type',
            new_name='user_types',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='bio',
        ),
    ]
