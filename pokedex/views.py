from django.shortcuts import render
from .models import *

# Create your views here.

def mostrarPokemons(request):
    pokemons = Pokemon.objects.all()

    contexto = {
        "todos_pokemons": pokemons,
    }
    return render(request, 'pokemon.html', contexto)
