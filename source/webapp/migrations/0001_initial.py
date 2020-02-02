# Generated by Django 2.1 on 2019-12-08 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('type', models.CharField(choices=[('ebook', 'e-version'), ('pbook', 'print version')], default='pbook', max_length=50, verbose_name='Статус')),
                ('author', models.CharField(max_length=200, verbose_name='Автор')),
                ('link', models.CharField(blank=True, max_length=200, verbose_name='Ссылка')),
                ('amount', models.IntegerField(blank=True, verbose_name='Количество')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('delivered', 'Доставлен'), ('canceled', 'Отменён')], default='new', max_length=20, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Издатель')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='webapp.Publisher'),
        ),
    ]
