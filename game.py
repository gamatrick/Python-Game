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
    print(f"Monstre '{nom}' ajouté (ID: {result.inserted_id})")
    return result.inserted_id

# Fonction pour ajouter un héros
def ajouter_hero(nom, atk, defense, pv):
    nouveau_hero = {'name': nom, 'ATK': atk, 'DEF': defense, 'PV': pv}
    result = hero.insert_one(nouveau_hero)
    print(f"Héros '{nom}' ajouté (ID: {result.inserted_id})")
    return result.inserted_id

def menu():
    print("==========Menu:===========")
    print("1. choisir un héros")
    print("2. Ajouter un héros")
    print("3. Ajouter un monstre")
    print("4. Sauvegarder")
    print("5. Quitter")


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
    def __init__(self, hero_collection):
        self.hero_collection = hero_collection

    def run(self):
        while True:
            menu()
            choix = input("Choisissez une option: ")
            if choix == '1':
                print("Choisir un héros :")
                for h in self.hero_collection.find():
                    print(f"- {h['name']} (ATK: {h['ATK']}, DEF: {h['DEF']}, PV: {h['PV']})")
                
                choix_hero = input("Nom de l'héros choisi: ")
                hero = self.hero_collection.find_one({'name': choix_hero})
                if hero:
                    print(f"Vous avez choisi l'héros {hero['name']} avec {hero['PV']} PV, {hero['ATK']} ATK et {hero['DEF']} DEF.")
                else:
                    print("Héros introuvable.")

            elif choix == '2':
                nom = input("Nom de l'héros: ")
                atk = int(input("ATK de l'héros: "))
                def_ = int(input("DEF de l'héros: "))
                pv = int(input("PV de l'héros: "))
                ajouter_hero(nom, atk, def_, pv)
            elif choix == '3':
                nom = input("Nom du monstre: ")
                atk = int(input("ATK du monstre: "))
                def_ = int(input("DEF du monstre: "))
                pv = int(input("PV du monstre: "))
                ajouter_monstre(nom, atk, def_, pv)
            elif choix == '4':
                print("Sauvegarde en cours...")
                print("Sauvegarde not found!!!!!!!!!!!!!!!!")
                
            elif choix == '5':
                print("Quitter le jeu.")
                break
