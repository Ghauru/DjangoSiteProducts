from django.shortcuts import render, get_object_or_404
from .models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response


def index(request):
    p = get_object_or_404(Product, pk=2)
    return render(request, 'comp/index.html', {'product': p})

def about(request):
    return render(request, 'comp/about.html')

def site_help(request):
    return render(request, 'comp/help.html')

def compare(request):
    name = request.GET['name']
    product = get_object_or_404(Product.objects.all(), name=name)
    product = model_to_dict(product)
    serializer = ProductSerializer(data=product)
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
    return Response(data)

