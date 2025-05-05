# adapters/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('order/', views.order_view, name='order'),
    path('my-orders/', views.my_orders_view, name='my_orders'),
]
