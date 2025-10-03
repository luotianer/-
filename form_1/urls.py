# form_1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_list),
    path('order/', views.create_order),
]