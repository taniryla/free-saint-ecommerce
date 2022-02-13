from django.shortcuts import render
from django.http import HttpResponse


def store(request):
    return render(request, 'store/store.html')


def cart(request):
    return render(request, 'store/cart.html')


def product_detail(request):
    return render(request, 'store/product_detail.html')
