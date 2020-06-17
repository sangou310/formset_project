from django.shortcuts import render, redirect
from django.views.generic import ListView

from app.forms import OrderCreateFormset
from app.models import Order, Stock


class OrderListView(ListView):
    model = Order
    context_object_name = 'order_list'
    template_name = 'app/order_list.html'


def add(request):
    formset = OrderCreateFormset(request.POST or None)
    # 削除チェックボックスにclassを設定
    for form in formset:
        form.fields['DELETE'].widget.attrs['class'] = 'form-check'

    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('app:order_list')

    context = {
        'formset': formset,
        'stock_list': Stock.objects.all(),
    }
    return render(request, 'app/order_add.html', context)
