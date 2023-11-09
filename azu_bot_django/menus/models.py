from django.db import models
from azu_bot_django.settings import (
    MAX_CHAR_LENGHT,
    MAX_DECIMAL_LENGHT,
    MAX_DIGIT_LENGHT
)
from django.db.models import UniqueConstraint


class Set(models.Model):
    name = models.CharField(
        'Название сета',
        max_length=MAX_CHAR_LENGHT,
        unique=True
    )
    description = models.CharField(
        'Описание сета',
        max_length=MAX_CHAR_LENGHT
    )
    dishes = models.ManyToManyField(
        "Dish",
        through="SetDish",
        verbose_name='Блюда',
        blank=True
    )
    price = models.DecimalField(
        verbose_name='Цена сета',
        decimal_places=MAX_DECIMAL_LENGHT,
        max_digits=MAX_DIGIT_LENGHT
    )

    class Meta:
        verbose_name = 'Сет'
        verbose_name_plural = 'Сеты'
        ordering = ("price", "name",)

    def __str__(self):
        return f'Сет {self.name} по цене {self.price}'


class Dish(models.Model):
    name = models.CharField(
        'Название блюда',
        max_length=MAX_CHAR_LENGHT
    )
    description = models.CharField(
        'Описание блюда',
        max_length=MAX_CHAR_LENGHT
    )

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ("name",)
        constraints = [
            UniqueConstraint(
                fields=('name', 'description',),
                name='unique_name_description'
            ),
        ]

    def __str__(self):
        return f'Блюдо {self.name}'


class SetDish(models.Model):
    """
    Связующий класс между Сетами(Set) и блюдами(Dish)
    """
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        verbose_name='Количество блюд в сете')

    class Meta:
        verbose_name = 'Блюд в сете'
        verbose_name_plural = 'Блюд в сете'
        constraints = [
            UniqueConstraint(
                fields=('set', 'dish'),
                name='unique_set_dish'
            ),
        ]

    def __str__(self):
        return f'{self.quantity} {self.dish.name}'
