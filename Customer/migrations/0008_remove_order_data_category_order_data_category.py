# Generated by Django 4.1.7 on 2023-04-06 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0007_order_data_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_data',
            name='category',
        ),
        migrations.AddField(
            model_name='order_data',
            name='category',
            field=models.CharField(default='', max_length=10),
        ),
    ]