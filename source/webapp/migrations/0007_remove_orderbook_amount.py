# Generated by Django 2.1 on 2019-12-14 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20191214_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderbook',
            name='amount',
        ),
    ]
