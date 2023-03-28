# Generated by Django 3.2 on 2023-01-04 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0013_student_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=48)),
                ('authors', models.ManyToManyField(to='dcim.Author')),
            ],
        ),
    ]
