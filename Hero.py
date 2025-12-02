from pymongo import MongoClient
from bson.objectid import ObjectId

class Hero:
    def __init__(self, name, ATK, DEF, PV):
        self.name = name
        self.ATK = ATK
        self.DEF = DEF
        self.PV = PV
        
    def choix_hero(self):
        hero = Hero(name, ATK, DEF, PV)
        print("Vous avez choisi le hero", hero.name)
        return hero