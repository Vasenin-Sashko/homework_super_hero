from tkinter import N
import requests

token = '2619421814940190'

urls = [
        f"https://superheroapi.com/api/{token}/search/Hulk", 
        f"https://superheroapi.com/api/{token}/search/Captain%America",
        f"https://superheroapi.com/api/{token}/search/Thanos"
] 

# обращаемся на сайт за характеристиками каждого героя и определяем его интеллект:
super_hero = []
for url in urls:
    responce = requests.get(url)
    r = responce.json()
    try:
        for parameter in r['results']:
            super_hero.append({
                'name': parameter['name'],
                'intelligence': parameter['powerstats']['intelligence'],
            })
    except KeyError:
        print(f"Проверте ссылки urls: {urls}")
# определяем какой герой самый умный:    
    intelligence_best = 0
    for intelligence_super_hero in super_hero:
        if intelligence_best < int(intelligence_super_hero['intelligence']):
            intelligence_best = int(intelligence_super_hero['intelligence'])
            name = intelligence_super_hero['name']

print(f"Самый умный герой: {name}, его интеллект = {intelligence_best}.")
