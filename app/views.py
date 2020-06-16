from django.shortcuts import render, redirect
from django.views.generic import ListView

from app.forms import OrderCreateFormset
from app.models import Order, Stock


class OrderListView(ListView):
    model = Order


def add(request):
    formset = OrderCreateFormset(request.POST or None)
    for form in formset:
        form.fields['DELETE'].widget.attrs['class'] = 'form-check align-middle'

    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('app:order_list')

    context = {
        'formset': formset,
        'stock_list': Stock.objects.all(),
    }
    return render(request, 'app/order_add.html', context)
