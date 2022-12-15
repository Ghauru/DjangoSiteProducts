from django.urls import path
from .views import ProductView, MarketView, AllView


urlpatterns = [
    path('', AllView.as_view()),
    path('products/', ProductView.as_view()),
    path('markets/', MarketView.as_view()),
]
