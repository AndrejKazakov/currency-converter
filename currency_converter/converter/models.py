from django.db import models


class Currency(models.Model):
    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name='Наименование')
    symbol = models.CharField(
        max_length=3,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Обозначение')
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name='Курс валюты')

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.name
