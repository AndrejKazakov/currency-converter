from django import forms
from .models import Currency


class ConverterForm(forms.Form):
    amount = forms.DecimalField(
        label='Сумма',
        max_digits=10,
        decimal_places=2
    )
    from_currency = forms.ModelChoiceField(
        queryset=Currency.objects.all(),
        label='Исходная валюта'
    )
    to_currency = forms.ModelChoiceField(
        queryset=Currency.objects.all(),
        label='Конечная валюта'
    )
