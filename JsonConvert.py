import json
import os

path ='pokemonUnite/static/pokemonUnite/img'
files = os.listdir(path)
list = []
i = 1

for f in files:
    pok_name = f[f.find('roster-')+7:f.find('.png')]
    print(pok_name)

    list.append(
      {
          'model': 'pokemonUnite.pokemon',
          'pk': i,
          'fields': {

              'image': 'pokemonUnite/img/' + f
          }
      }
    )

    i += 1

# print(list)
# print(len(list))

with open('test4.json', 'w') as outfile:
    json.dump(list, outfile)