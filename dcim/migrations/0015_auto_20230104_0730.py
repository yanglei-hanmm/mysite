# Generated by Django 3.2 on 2023-01-04 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0014_author_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school_class',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='SchoolClass',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
