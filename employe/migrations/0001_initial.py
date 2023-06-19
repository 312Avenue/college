# Generated by Django 4.1.3 on 2022-12-15 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pulpit',
            fields=[
                ('slug', models.SlugField(blank=True, max_length=155, primary_key=True, serialize=False, unique=True, verbose_name='Поле слаг')),
                ('puplit', models.CharField(max_length=155, verbose_name='Кафедра')),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедры',
            },
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=155, verbose_name='Фамилия')),
                ('otch', models.CharField(max_length=155, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('description', models.TextField(verbose_name='Описание')),
                ('post', models.CharField(max_length=155, verbose_name='Должность')),
                ('img', models.ImageField(upload_to='employe', verbose_name='Фото')),
                ('puplit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pulpit', to='employe.pulpit', verbose_name='Кафедра')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]