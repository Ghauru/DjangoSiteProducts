from django.urls import path, re_path

from . import views

urlpatterns = [
    path('<int:p_k>/', views.get_market_by_number),
    re_path(r'^search/(?P<name>[a-z]+)/$', views.get_market_by_name)
]