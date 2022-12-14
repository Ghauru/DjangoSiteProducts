from django.urls import path
from . import views

urlpatterns = [
    path('<int:p_k>', views.get_product_by_number),
    path('search/', views.get_product_by_name)
]