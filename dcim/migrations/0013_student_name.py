# Generated by Django 3.2 on 2023-01-04 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0012_schoolclass_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
