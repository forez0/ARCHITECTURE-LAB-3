# adapters/views.py
from django.shortcuts import render, redirect
from .forms import OrderForm
from infrastructure.repositories import DjangoRepository
from domain.services import order_book
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView

# Імпортуємо моделі через apps
BookModel = apps.get_model('adapters', 'BookModel')
OrderModel = apps.get_model('adapters', 'OrderModel')


def index(request):
    return render(request, 'index.html')

@login_required
def order_view(request):
    repo = DjangoRepository()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            order_book(request.user, book, repo)
            return redirect('my_orders')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})

@login_required
def my_orders_view(request):
    repo = DjangoRepository()
    books = repo.get_user_orders(request.user.id)
    return render(request, 'orders.html', {'books': books})

# Форма реєстрації
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Логін через стандартну форму
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm

