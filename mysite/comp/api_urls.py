from django.urls import path
from .views import ProductView, MarketView

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('markets/', MarketView.as_view()),
]
