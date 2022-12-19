from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('help', views.site_help, name='help'),
    path('compare/', views.compare),
    path('search', views.search_view)
]
