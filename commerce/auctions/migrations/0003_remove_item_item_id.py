# Generated by Django 4.1.7 on 2023-03-18 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_id',
        ),
    ]
