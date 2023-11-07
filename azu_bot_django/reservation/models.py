from django.db import models
from cafe.models import Cafe
from menu.models import Set
from azu_bot_django.settings import MAX_CHAR_LENGHT
from tables.models import ReservationTable
from django.db.models import UniqueConstraint


class Reservation(models.Model):
    cafe = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        related_name='res_cafe',
        verbose_name='В кафе'
    )
    tables = models.ManyToManyField(
        ReservationTable,
        verbose_name='Столы',
        related_name='tables'
    )
    sets = models.ManyToManyField(
        Set,
        through='OrderSets',
        verbose_name='Заказы'
    )
    date = models.DateField(
        'Дата бронирования'
    )
    name = models.CharField(
        'Имя клиента',
        max_length=MAX_CHAR_LENGHT
    )
    number = models.CharField(
        'Номер телефона клиента',
        max_length=MAX_CHAR_LENGHT
    )

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'
        ordering = ("date",)

    def __str__(self):
        return f'В кафе {self.cafe}, для {self.name} на {self.date}'


class OrderSets(models.Model):
    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name='order_sets',
        verbose_name='Бронь'
    )
    set = models.ForeignKey(
        Set,
        on_delete=models.CASCADE,
        verbose_name='Сет'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество сета'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        constraints = [
            UniqueConstraint(
                fields=('reservation', 'set'),
                name='unique_reservation_set'
            ),
        ]

    def __str__(self):
        return f'Заказ {self.set} в количестве {self.quantity}'
