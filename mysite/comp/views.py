from django.shortcuts import render
from .models import Product
from django.http import Http404


def index(request):
    try:
        p = Product.objects.get()
    except Product.DoesNotExist:
        raise Http404("Товар не найден")
    return render(request, 'comp/index.html', {'product': p})

def about(request):
    return render(request, 'comp/about.html')


def site_help(request):
    return render(request, 'comp/help.html')