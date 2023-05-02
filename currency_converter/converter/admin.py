from django.contrib import admin
from .models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'symbol', 'rate')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Currency, CurrencyAdmin)
