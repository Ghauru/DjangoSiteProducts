from django.shortcuts import render, get_object_or_404
from .models import Product, Market
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MarketSerializer, ProductSerializer
from rest_framework.decorators import api_view

class ProductView(APIView):
    def get(self, request):
        product_list = []
        products = Product.objects.all()
        for item in products:
            product_list.append(model_to_dict(item))
        return Response({"products": product_list})


class MarketView(APIView):
    def get(self, request, p_k):
        markets = Market.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = MarketSerializer(markets, many=True)
        return Response({"markets": serializer.data})
    def post(self, request):
        market = request.data.get('articles')
        # Create an article from the above data
        serializer = MarketSerializer(data=market)
        if serializer.is_valid(raise_exception=True):
            market_saved = serializer.save()
        return Response({"success": "Market '{}' created successfully".format(market_saved.title)})

def index(request):
    p = get_object_or_404(Product, pk=2)
    return render(request, 'comp/index.html', {'product': p})

def about(request):
    return render(request, 'comp/about.html')


def site_help(request):
    return render(request, 'comp/help.html')


@api_view(('GET',))
def get_market_by_number(request, p_k):
    market = get_object_or_404(Market.objects.all(), pk=p_k)
    market = model_to_dict(market)
    serializer = MarketSerializer(data=market)
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
    return Response(data)


@api_view(('GET',))
def get_market_by_name(request, name):
    name = name[name.find('name=')+5:]
    serializer = MarketSerializer(name=name)
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
    return Response(data)


@api_view(('GET',))
def get_product_by_number(request, p_k):
    product = get_object_or_404(Product.objects.all(), pk=p_k)
    product = model_to_dict(product)
    serializer = ProductSerializer(data=product)
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
    return Response(data)


@api_view(('GET',))
def get_product_by_name(request):
    name = request.GET['name']
    product = get_object_or_404(Product.objects.all(), name=name)
    product = model_to_dict(product)
    serializer = ProductSerializer(data=product)
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
    return Response(data)


