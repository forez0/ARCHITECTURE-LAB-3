# library_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from adapters import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('order/', views.order_view, name='order'),
    path('my-orders/', views.my_orders_view, name='my_orders'),
    path('register/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
