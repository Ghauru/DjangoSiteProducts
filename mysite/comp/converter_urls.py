from django.urls import path, re_path

from . import views

urlpatterns = [
    path('<int:p_k>/', views.get_market_by_number),
    path('<str:name>', views.get_market_by_name)
]