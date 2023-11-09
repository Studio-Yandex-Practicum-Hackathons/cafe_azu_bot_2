from django.db import models
from cafes.models import Cafe


class Table(models.Model):
    cafe = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        related_name='table_cafe',
        verbose_name='В кафе'
    )
    quantity = models.PositiveSmallIntegerField(
        'Размер стола'
    )

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'
        ordering = ("cafe", "quantity",)

    def __str__(self):
        return f'Cтол на в {self.cafe} размером {self.quantity} человек'


class ReservationTable(models.Model):
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        verbose_name='Стол'
    )
    date = models.DateField(
        'Дата бронирования'
    )

    class Meta:
        verbose_name = 'Бронь стола'
        verbose_name_plural = 'Брони стола'

    def __str__(self):
        return f'{self.table} занят на {self.date}'
