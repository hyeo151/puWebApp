from django.urls import path
from . import views

app_name = 'pokemonUnite'

urlpatterns = [
    path('all', views.list_all_pok, name='all_pokemon'),
    path('all/<int:pk>', views.pok_detail, name='pokemon_detail')
]
