from django.urls import path
from . import views

urlpatterns = [
    path('ufpb/', views.index, name='index'),
    path('MinhasNudes/', views.easter_egg, name='easter_egg'),
    ]
