# Generated by Django 3.2 on 2022-12-28 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0004_auto_20221228_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicessku',
            name='dc_id',
        ),
    ]
