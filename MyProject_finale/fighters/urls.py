from django.urls import path
from . import views

urlpatterns = [
    path('', views.fighters, name= 'home'),
    path('statistiche', views.statistiche),
    path('input/', views.input, name='input'),
    path('vota/', views.vota_fighter, name='vota_fighter'),
]