# Generated by Django 4.1.7 on 2023-06-04 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_title', models.CharField(max_length=50, verbose_name='Название фильма')),
                ('producer', models.CharField(max_length=100, verbose_name='Режиссер')),
                ('duration', models.TimeField(verbose_name='Продолжительность')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_title', models.CharField(max_length=50, verbose_name='Название зала')),
                ('quantity_pc', models.IntegerField(verbose_name='Количество мест')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_s', models.TimeField(verbose_name='Время')),
                ('ticket_price', models.FloatField(verbose_name='Цена билета')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.film')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.hall')),
            ],
            options={
                'verbose_name': 'Сеанс',
                'verbose_name_plural': 'Сеансы',
            },
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField(verbose_name='Место')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.session')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
            },
        ),
    ]