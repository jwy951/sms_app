# Generated by Django 2.2.13 on 2021-01-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0007_auto_20210118_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryreport',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
