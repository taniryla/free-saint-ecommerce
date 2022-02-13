from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


# placed here temporarily until order category app are created


def category(request):
    return HttpResponse('<h1>Category /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def search(request):
    return HttpResponse('<h1>Search /ᐠ｡‸｡ᐟ\ﾉ</h1>')
