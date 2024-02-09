# Generated by Django 4.2.10 on 2024-02-07 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0006_remove_userprofileinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='bio',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_users.user'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]