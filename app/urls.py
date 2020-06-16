from django.urls import path

from app.views import OrderListView, add

app_name = 'app'
urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('add/', add, name='order_add'),
]
