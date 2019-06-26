from django.contrib import admin
from django.urls import path
from .views import *

app_name = "pokedex"

urlpatterns = [
    path("listar/", listarPokemons, name="mostrar_pokemons"),
<<<<<<< HEAD
    path("listar/<str:ordenacao>/", listarPokemons, name="mostrar_pokemons"),
    path("pokemon/<int:idpokemon>/", umPokemon, name="um_pokemon"),
    path("time/", timeMaisForte, name="time_forte")
=======
    path("pokemon/<int:idpokemon>/", umPokemon, name="um_pokemon")
>>>>>>> f9d9383f070a099bbde7307532d6e95a34dce394
    ]
