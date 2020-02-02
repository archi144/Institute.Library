# Generated by Django 2.1 on 2019-12-10 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_orderbook_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('На рассмотрении', 'На рассмотрении'), ('Одобрена', 'Одобрена'), ('Отклонена', 'Отклонена')], default='На рассмотрении', max_length=20),
        ),
        migrations.AlterField(
            model_name='request',
            name='type',
            field=models.CharField(choices=[('На списание', 'На списание'), ('На закупку', 'На закупку')], default='На закупку', max_length=20),
        ),
    ]