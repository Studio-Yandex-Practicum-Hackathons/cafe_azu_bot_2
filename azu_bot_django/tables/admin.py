from django.contrib import admin
from .models import Table, ReservationTable


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("cafe", "quantity")


@admin.register(ReservationTable)
class ReservationTableAdmin(admin.ModelAdmin):
    list_display = ("table", "date")
