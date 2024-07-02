import requests
import json
import os

def clear ():
    os.system('cls' if os.name == 'nt' else 'clear')

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

poke_data = response.json()

print(poke_data['name'].title())
print(poke_data['abilities'])


def fetch_pokemon_data():
    pokemon1 = input("Who is the first pokemon are you looking for?")
    pokemon2 = input("Who is the second pokemon you are looking for?")
    pokemon3 = input("Who is the third pokemon you are looking for?")
    response1 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon1.lower()}")
    response2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon2.lower()}")
    response3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon3.lower()}")
    if response1.status_code == 200:
        poke1_data = response1.json()
        poke1_dict = {
            "name": poke1_data['name'],
            "abilities": poke1_data["abilities"],
            "weight": poke1_data["weight"]
        }
    if response2.status_code == 200:
        poke2_data = response2.json()
        poke2_dict = {
            "name": poke2_data['name'],
            "abilities": poke2_data["abilities"],
            "weight": poke2_data["weight"]
        }
    if response3.status_code == 200:
        poke3_data = response3.json()
        poke3_dict = {
            "name": poke3_data['name'],
            "abilities": poke3_data["abilities"],
            "weight": poke3_data["weight"]
        }
    
    if poke1_dict and poke2_dict and poke3_dict:
        average_weight = (poke1_dict["weight"] + poke2_dict["weight"] + poke3_dict["weight"])/3
        clear()
        return f"Pokemon 1: {poke1_dict},\n\nPokemon 2: {poke2_dict},\n\nPokemon 3: {poke3_dict},\n\nAverage weight: {average_weight}"
    else:
        print("One or more requests failed. Please try again.")

print(fetch_pokemon_data())



