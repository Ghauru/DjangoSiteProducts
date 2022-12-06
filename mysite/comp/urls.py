from django.urls import path
from .views import ProductView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('help', views.site_help, name='help'),
]
