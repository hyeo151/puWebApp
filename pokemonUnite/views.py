from django.shortcuts import render
from pokemonUnite.models import Pokemon


# from django.http import HttpResponse

# Create your views here.
def list_all_pok(request):
    all_pokemon = Pokemon.objects.all()
    return render(request, 'pokemonUnite/all_pokemon.html', {'all_pokemon': all_pokemon})


def pok_detail(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    return render(request, 'pokemonUnite/pokemon_detail.html', {'pokemon': pokemon})
