from django.shortcuts import render
from .forms import ConverterForm


def convert(request):
    if request.method == 'POST':
        form = ConverterForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_currency = form.cleaned_data['from_currency']
            to_currency = form.cleaned_data['to_currency']
            rate = to_currency.rate / from_currency.rate
            converted_amount = f'{(amount * rate):.2f}'
    else:
        form = ConverterForm()
        converted_amount = None
    return render(
        request,
        'converter.html',
        {'form': form, 'converted_amount': converted_amount}
    )
