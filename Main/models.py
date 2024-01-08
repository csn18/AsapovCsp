from django.contrib.auth.models import User
from django.db import models


class PerformanceUnit(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'


class PerformanceName(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название показателя'
        verbose_name_plural = 'Названия показателей'


class Performance(models.Model):
    cadet = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.ForeignKey(PerformanceName, on_delete=models.PROTECT)
    value = models.CharField(verbose_name='Показатель', max_length=255)
    unit = models.ForeignKey(PerformanceUnit, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', max_length=4096, blank=True)

    class Meta:
        verbose_name = 'Показатель курстанат'
        verbose_name_plural = 'Показатели курсантов'
