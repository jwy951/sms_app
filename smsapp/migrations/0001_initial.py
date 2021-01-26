# Generated by Django 2.2.13 on 2021-01-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmsLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('statusCode', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('text', models.CharField(max_length=255)),
                ('messageId', models.CharField(max_length=100)),
            ],
        ),
    ]