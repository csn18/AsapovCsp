# Generated by Django 5.0.1 on 2024-01-08 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_performancename_performance_cadet_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformanceUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единицы измерения',
            },
        ),
        migrations.AlterModelOptions(
            name='performancename',
            options={'verbose_name': 'Название показателя', 'verbose_name_plural': 'Названия показателей'},
        ),
        migrations.AlterField(
            model_name='performance',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.performanceunit'),
        ),
    ]
