from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017')
db = client['game_db']
monstre = db['monstre']
hero = db['hero']
sauvegarde = db['sauvegarde']


monstre.delete_many({})
hero.delete_many({})  

# Fonction pour ajouter un monstre
def ajouter_monstre(nom, atk, defense, pv):
    nouveau_monstre = {'name': nom, 'ATK': atk, 'DEF': defense, 'PV': pv}
    result = monstre.insert_one(nouveau_monstre)
    print(f"✅ Monstre '{nom}' ajouté (ID: {result.inserted_id})")
    return result.inserted_id

# Fonction pour ajouter un héros
def ajouter_hero(nom, atk, defense, pv):
    nouveau_hero = {'name': nom, 'ATK': atk, 'DEF': defense, 'PV': pv}
    result = hero.insert_one(nouveau_hero)
    print(f"✅ Héros '{nom}' ajouté (ID: {result.inserted_id})")
    return result.inserted_id

def menu():
    print("==========Menu:===========")
    print("1. choisir un héros")
    print("2. Ajouter un héros")
    print("3. Ajouter un monstre")
    print("4. Sauvegarder")
    print("4. Quitter")


# créations de la BDD monstre si elle n'existe pas
if monstre.count_documents({}) == 0:
    monstre_data =[
        {'name': 'Gobelin', 'ATK': 17, 'DEF': 15, 'PV': 120},
        {'name': 'Orc', 'ATK': 12, 'DEF': 6, 'PV': 45},
        {'name': 'Squelette', 'ATK': 10, 'DEF': 5, 'PV': 35}
    ]

    monstre.insert_many(monstre_data)
    print("Monstre ajouté")
else:
    print("Monstre deja ajouté: ", monstre.count_documents({}))
     
# créations de la BDD hero si elle n'existe pas   
if hero.count_documents({}) == 0:
    hero_data =[
        {'name': 'Guerrier', 'ATK': 15, 'DEF': 10, 'PV': 50},
        {'name': 'Sorcier', 'ATK': 25, 'DEF': 3, 'PV': 70},
        {'name': 'Berserker', 'ATK': 23, 'DEF': 6, 'PV': 105}
    ]

    hero.insert_many(hero_data)
    print("Hero ajouté")
else:
    print("Hero deja ajouté: ", hero.count_documents({}))
    
   
 
class Game:
    while True:
        menu()
        choix = input("Choisissez une option: ")
        if choix == '1':
            print ("choisir un héros :")
            print (hero.find())
            