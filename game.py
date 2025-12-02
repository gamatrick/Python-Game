from pymongo import MongoClient
from bson.objectid import ObjectId
from Hero import Hero


def list_hero(self):
    return list(self.hero.find())

def menu():
    print("\nMenu :\n"
        "1. Choisir un Hero\n"
        "2. Historique de partie\n"
        "3. Quitter\n"
    )

    while True:
        print (menu)
        
        if input("Que voulez-vous faire ? ") == "1":
            hero = Hero(name, ATK, DEF, PV)
            print("Vous avez choisi le hero", hero.name)
            return hero
    
