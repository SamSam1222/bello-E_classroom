# Generated by Django 4.0.4 on 2022-04-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_workingdays_timeslots_slotsubject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='position',
            field=models.PositiveSmallIntegerField(verbose_name='week.'),
        ),
    ]
