# Generated by Django 5.0.1 on 2024-01-08 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('value', models.CharField(max_length=255, verbose_name='Показатель')),
                ('unit', models.CharField(max_length=255, verbose_name='Единица')),
                ('description', models.TextField(max_length=4096, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Показатель курстанат',
                'verbose_name_plural': 'Показатели курсантов',
            },
        ),
    ]