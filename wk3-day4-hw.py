
import requests
from pprint import pprint

your_pokemon = None
pokemon_list = []
p = {}


class Pokemon:
    global your_pokemon, p
    def __init__(self, poke_name, type1, ability1, ability2, height, weight):
        
        self.poke_name = poke_name
        self.type1 = type1
        self.ability1 = ability1
        self.ability2 = ability2
        self.height = height
        self.weight = weight
        
    def __repr__(self):
        return f"{self.poke_name}"   
        

class Pokedex:
    global your_pokemon, p
    def __init__(self):

        self.all_pokemon = []
                
    def add_pokemon(self, your_pokemon):
        self.endpoint = f"https://pokeapi.co/api/v2/pokemon/{your_pokemon}/"
        
        self.poke_results = requests.get(self.endpoint).json()

        p = Pokemon(
        poke_name = self.poke_results["name"],
        type1 = self.poke_results["types"][0]["type"]["name"],
        ability1 = self.poke_results["abilities"][0]["ability"]["name"],
        ability2 = self.poke_results["abilities"][1]["ability"]["name"],
        height = self.poke_results["height"],
        weight = self.poke_results["weight"],
        )
        self.all_pokemon.append(p)

    def show_attributes(self):
        detail_name = input("Which one? ")
        for each in self.all_pokemon:
            if each.poke_name == detail_name: 
                print(each.__dict__)
        selection()

trial1 = Pokedex()


def selection():
    global your_pokemon
    choice = input("""
What do you want to do? 
Type 'add' to add a pokemon to your pokedex. 
Type 'show' to view a list of your pokemon.
Type 'details' to see attributes of specific pokemon. 
Type 'quit' to exit.
Add/Show/Quit: """)

    if choice == 'add':
        your_pokemon = input("Choose a pokemon to add to your Pokedex: ")
        trial1.add_pokemon(your_pokemon)
        selection()

    elif choice == 'show':
        print(trial1.all_pokemon)
        selection()

    elif choice == 'details':
        trial1.show_attributes()
    
    elif choice == "quit":
        quit()

     
        print(p)
        selection()


     
selection()

