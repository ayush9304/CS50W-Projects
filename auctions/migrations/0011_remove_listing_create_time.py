# Generated by Django 3.0.8 on 2020-07-22 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20200722_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='create_time',
        ),
    ]
