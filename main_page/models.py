from django.db import models
from django.contrib.auth.models import User

class Main(models.Model):
    nickname = models.CharField(max_length=100, verbose_name='Кличка')
    age = models.FloatField(blank=True, verbose_name='Возраст, лет')
    date_arrival = models.DateField(verbose_name='Дата прибытия')
    weight = models.FloatField(blank=True, verbose_name='Вес, кг')
    height = models.FloatField(blank=True, verbose_name='Рост, см')
    special_mark = models.TextField(blank=True, verbose_name='Отличительные черты')

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Паспорт животного'
        verbose_name_plural = 'Паспорта животных'
        ordering = ['-date_arrival']

