# Generated by Django 3.1.2 on 2020-11-19 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0008_ticket_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='email',
            field=models.EmailField(blank=True, max_length=45),
        ),
        migrations.AddField(
            model_name='ticket',
            name='mobile',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
