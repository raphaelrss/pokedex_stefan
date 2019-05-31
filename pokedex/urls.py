from django.contrib import admin
from django.urls import path
from .views import *

app_name = "pokedex"

urlpatterns = [
    path("listar/", listarPokemons, name="mostrar_pokemons"),
    path("listar/<str:ordenacao>/", listarPokemons, name="mostrar_pokemons"),
    path("pokemon/<int:idpokemon>/", umPokemon, name="um_pokemon")
    ]
