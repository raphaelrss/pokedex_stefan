from django.contrib import admin
from django.urls import path
from .views import *
from django import views

urlpatterns = [
    path('', views.mostrarPokemons, name='mostrar_pokemons')
]