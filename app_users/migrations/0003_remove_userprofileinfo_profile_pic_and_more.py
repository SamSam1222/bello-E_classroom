# Generated by Django 4.2.10 on 2024-02-07 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_contact_rename_user_profile_userprofileinfo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
