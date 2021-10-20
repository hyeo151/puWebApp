import json
import os

# get file object
f = open("pokemonExample.txt", "r")
list = []
i = 0
dic = {}

while True:
    # read next line
    l = f.readline()
    if l.find(":"):

        sub = l[l.find(":") + 1:].strip()

        # finding price part
        if sub.find('/') != -1:
            prices = sub.split('/')
            price_aeos = int(prices[0][prices[0].find('png') + 4:].strip())
            price_gems = int(prices[1][prices[1].find('png')+4:].strip())
            i += 2
            dic['price_aeos'] = price_aeos
            dic['price_gems'] = price_gems
            continue

        # finding rank part
        if sub.find('Rank') != -1:
            string_list = sub.split()
            sub = string_list[0]

        # find Description part
        if sub.find('"') != -1:
            sub = sub.replace('"', '')

        if sub != '':
            if i == 0:
                dic['name'] = sub
            elif i == 1:
                dic['tier'] = sub
            elif i == 2:
                dic['Role'] = sub
            elif i == 3:
                dic['attack_type'] = sub
            elif i == 4:
                dic['damage_type'] = sub
            elif i == 5:
                dic['difficulty'] = sub
            elif i == 8:
                dic['desc'] = sub
                list.append(dic)
                dic = {}
                i = 0
                continue
            i += 1
    if not l:
        break


def removingSpecialChar(s):
    s = s.lower()

    # initializing special characters
    special_char = '.@_!#$%^&*()<>?/\|}{~:;[]- '

    # using filter() to remove special characters
    new_string = ''.join((filter(lambda i: i not in special_char, s)))

    # print string without special characters
    print('removed special Char string:', new_string)
    return new_string

# search list of dictionary and find the right dictionary using name
def search_list(list, pok_name):
    print("_________search List______________")
    final_dic = {}
    pok_name = removingSpecialChar(pok_name)

    for d in list:
        print("******printing dic",d)
        print("________before calling removingSpecialChar(d[name])_______"+d['name'])
        lower_dname = removingSpecialChar(d['name'])
        print("________After calling removingSpecialChar(d[name])_______"+d['name'])
        print("Text lower_dname:" + lower_dname)
        print("FilePath pok_name:" + pok_name)
        if lower_dname == pok_name:
            print("matched!")
            final_dic = d
            break

    return final_dic


# Reading image Files

path ='pokemonUnite/static/pokemonUnite/img'
files = os.listdir(path)
json_list = []
counter = 1

for f in files:
    print("_________looping files__________")
    pok_name = f[f.find('roster-')+7:f.find('.png')]

    pok_dic = search_list(list, pok_name)
    print('retunred___')
    print(pok_dic)
    json_list.append(
        {
            'model': 'pokemonUnite.pokemon',
            'pk': counter,
            'fields': {
                'name': pok_dic['name'],
                'desc': pok_dic['desc'],
                'attack_type': pok_dic['attack_type'],
                'damage_type': pok_dic['damage_type'],
                'tier': pok_dic['tier'],
                'difficulty': pok_dic['difficulty'],
                'image': 'pokemonUnite/img/' + f,
                'price_aeos': pok_dic['price_aeos'],
                'price_gems': pok_dic['price_gems']
            }
        }
    )

    counter += 1

with open('test6.json', 'w') as outfile:
    json.dump(json_list, outfile)
