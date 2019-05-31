from django.shortcuts import render
from .models import *

# Create your views here.


def listarPokemons(request, ordenacao = "nome"):
    pokemons = Pokemon.objects.all().order_by(ordenacao)

    contexto = {
        "todos_pokemons": pokemons,
    }
    return render(request, 'listar.html', contexto)


def umPokemon(request, idpokemon=None):
    pokemon = Pokemon.objects.get(id=idpokemon)
    contexto = {
        "pokemon": pokemon,
    }
    return render(request, 'pokemon.html', contexto)
