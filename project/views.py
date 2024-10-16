from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.forms.models import model_to_dict

from .forms import PizzaForm, OrderForm
from .models import Pizza, Order


def home_page(request: WSGIRequest):

    if request.method == "POST":
        form = PizzaForm(request.POST, request.FILES)

        if form.is_valid():
            form.create()

    pizzas = Pizza.objects.all()
    form = PizzaForm()

    context = {
        "pizzas": pizzas,
        "form": form,
    }

    return render(request, "home_page.html", context)


def orders_page(request: WSGIRequest):

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            form.create()

    orders = Order.objects.all()
    form = OrderForm()

    context = {
        "orders": orders,
        "form": form,
    }

    return render(request, "orders_page.html", context)
