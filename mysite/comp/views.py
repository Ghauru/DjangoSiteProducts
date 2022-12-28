from django.shortcuts import render, get_object_or_404
from .models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from api.serializers import ProductSerializer
from parser import wb_parser


def index(request):
    return render(request, 'comp/index.html')

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

def search_view(request):
    query = request.GET.get('query')
    try:
        product = Product.objects.filter(search_name__contains=query.lower())[0]
    except:
        max_words = wb_parser.full_parser(query)
        product = Product.objects.filter(search_name__contains=max_words, market_place='Wildberries')[0]
    return  render(request, 'comp/index.html', {'product': product})
