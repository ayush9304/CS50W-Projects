# Generated by Django 3.0.8 on 2020-07-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_listing_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='listing',
            name='create_time',
            field=models.DateTimeField(),
        ),
    ]
