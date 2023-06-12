# Generated by Django 4.1.7 on 2023-03-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_remove_item_current_bid_item_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='current_bid',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='starting_bid',
            field=models.FloatField(max_length=10),
        ),
    ]