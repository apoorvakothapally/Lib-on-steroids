# Generated by Django 2.1.9 on 2019-10-11 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20191011_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
    ]
