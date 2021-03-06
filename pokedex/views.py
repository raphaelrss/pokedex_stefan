from django.shortcuts import render
from .models import *

# Create your views here.


def listarPokemons(request):
    pokemons = Pokemon.objects.all()

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


def timeMaisForte(request):
    mais_fortes = Pokemon.objects.order_by('-pontos_de_ataque')[:6]
    contexto = {
        "pokemons_fortes": mais_fortes,
    }
    return render(request, 'pokemons_mais_fortes.html', contexto)
