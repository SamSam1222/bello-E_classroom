# Generated by Django 4.2.10 on 2024-02-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0013_rename_user_types_userprofileinfo_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('teachers', 'teachers'), ('students', 'students'), ('parents', 'parents')], default='students', max_length=10),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]