# Generated by Django 4.1.7 on 2023-03-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_item_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=150)),
                ('bid', models.CharField(max_length=10)),
            ],
        ),
    ]
