from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Dish, Set, SetDish


class SetDishInline(admin.TabularInline):
    model = SetDish
    extra = 1


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = (
        "name", "description",
        "price", "quantity",
        "display_image"
    )
    search_fields = ("name",)
    inlines = [SetDishInline]

    def view_dishes(self, obj):
        count = obj.dishes.count()
        if count == 1:
            short_description = 'блюда'
        else:
            short_description = 'блюд'
        url = (
            reverse("admin:menu_dish_changelist")
            + "?"
            + urlencode({"set__id": f"{obj.id}"})
        )
        return format_html(
            '<a href="{}">{} {}</a>', url, count, short_description
        )

    view_dishes.short_description = "Блюд"

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" height="50" />'.format(obj.image.url)
            )
        return None

    display_image.short_description = 'Изображение'


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
