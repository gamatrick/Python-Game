from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017')
db = client['game_db']
monstre = db['monstre']
hero = db['hero']
sauvegarde = db['sauvegarde']

if monstre.count_documents({}) == 0:
    monstre_data =[
        {'name': 'Gobelin', 'ATK': 17, 'DEF': 15, 'PV': 120}
    ]

    monstre.insert_many(monstre_data)
    print("Monstre ajouté")
else:
    print("Monstre deja ajouté")
        
if hero.count_documents({}) == 0:
    hero_data =[
        {'name': 'Guerrier', 'ATK': 15, 'DEF': 10, 'PV': 50}
    ]
 
    hero.insert_many(hero_data)
    print("Hero ajouté")
else:
    print("Hero deja ajouté")