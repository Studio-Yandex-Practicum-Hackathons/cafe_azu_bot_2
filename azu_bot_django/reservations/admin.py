from django.contrib import admin
from django.urls import reverse
from django import forms
from django.utils.html import format_html
from django.utils.http import urlencode
from django.core.exceptions import ValidationError


from reservations.models import Reservation, OrderSets


class OrderSetsInline(admin.TabularInline):
    model = OrderSets
    extra = 1


class ReservationForm(forms.ModelForm):
    def clean(self):
        """
        Проверка нахождения столов в забронированном кафе
        """
        super(ReservationForm, self).clean()
        tables_pk = self.cleaned_data['tables']
        for table in tables_pk:
            if self.cleaned_data['cafe'].id != table.table.cafe.id:
                raise ValidationError(
                    "Кафе и столы в кафе должны совпадать по местоположению"
                )


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("cafe", "view_tables", "view_order_sets",
                    "name", "number", "date")
    list_filter = ("date", )
    inlines = [OrderSetsInline]
    form = ReservationForm

    def get_queryset(self, request):
        """
        Персонал получит только брони его кафе,
        суперпользователя это не касается
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(cafe=request.user.cafe.id)

    def view_tables(self, obj):
        """
        Отображение количества забронированых столов
        и их вместительности на панели броней
        """
        count = obj.tables.count()
        quantity = ''
        if count == 1:
            short_description = ' Стол '
        elif 1 < count < 5:
            short_description = ' Стола '
        else:
            short_description = ' Столов '
        for table in obj.tables.all():
            if quantity:
                quantity += ', '
            quantity += str(table.table.quantity)

        return str(count) + short_description + 'на ' + quantity + ' человек'
    view_tables.short_description = 'Столов'

    def view_order_sets(self, obj):
        """
        Отображение количества заказанных сетов
        и переход на панель с этими заказами
        """
        count = obj.sets.count()
        if count == 1:
            short_description = 'Заказ'
        elif 1 < count < 5:
            short_description = 'Заказа'
        else:
            short_description = 'Заказов'
        url = (
            reverse("admin:reservations_ordersets_changelist")
            + "?"
            + urlencode({"reservations__id": f"{obj.id}"})
        )
        return format_html(
            '<a href="{}">{} {}</a>', url, count, short_description
        )
    view_order_sets.short_description = "Сетов"


@admin.register(OrderSets)
class OrderSetsAdmin(admin.ModelAdmin):
    pass
