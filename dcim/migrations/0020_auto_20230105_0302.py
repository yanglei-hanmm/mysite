# Generated by Django 3.2 on 2023-01-05 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0019_alter_dcrackinfo_unique_together'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dcinfo',
            table='dc',
        ),
        migrations.AlterModelTable(
            name='dcrack',
            table=None,
        ),
        migrations.AlterModelTable(
            name='dcrackinfo',
            table=None,
        ),
        migrations.AlterModelTable(
            name='devicessku',
            table=None,
        ),
        migrations.AlterModelTable(
            name='devicesspu',
            table=None,
        ),
        migrations.AlterModelTable(
            name='devicestype',
            table=None,
        ),
    ]