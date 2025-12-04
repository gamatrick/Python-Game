from pymongo import MongoClient

class DatabaseHandler:
    def __init__(self, uri='mongodb://localhost:27017', db_name='game_db'):
        client = MongoClient(uri)
        db = client[db_name]
        self.monsters = db['monstre']
        self.heroes = db['hero']
        self.saves = db['sauvegarde']

    def reset_collections(self):
        """Supprime tout le contenu des collections."""
        self.monsters.delete_many({})
        self.heroes.delete_many({})
        print("Base de données réinitialisée.")

    def init_data(self):
        """Insère les données de base pour les héros et monstres."""

        # Initialisation des monstres
        if self.monsters.count_documents({}) == 0:
            monster_data = [
                {'name': 'Gobelin', 'ATK': 17, 'DEF': 15, 'PV': 120},
                {'name': 'Orc', 'ATK': 12, 'DEF': 6, 'PV': 45},
                {'name': 'Squelette', 'ATK': 10, 'DEF': 5, 'PV': 35}
            ]
            self.monsters.insert_many(monster_data)
            print("Monstres ajoutés.")
        else:
            print(f"Monstres déjà présents : {self.monsters.count_documents({})}")

        # Initialisation des héros
        if self.heroes.count_documents({}) == 0:
            hero_data = [
                {'name': 'Guerrier', 'ATK': 15, 'DEF': 10, 'PV': 50},
                {'name': 'Sorcier', 'ATK': 25, 'DEF': 3, 'PV': 70},
                {'name': 'Berserker', 'ATK': 23, 'DEF': 6, 'PV': 105}
            ]
            self.heroes.insert_many(hero_data)
            print("Héros ajoutés.")
        else:
            print(f"Héros déjà présents : {self.heroes.count_documents({})}")

    def add_monster(self, name, atk, defense, pv):
        monster = {'name': name, 'ATK': atk, 'DEF': defense, 'PV': pv}
        result = self.monsters.insert_one(monster)
        print(f"Monstre '{name}' ajouté (ID: {result.inserted_id})")
        return result.inserted_id

    def add_hero(self, name, atk, defense, pv):
        hero = {'name': name, 'ATK': atk, 'DEF': defense, 'PV': pv}
        result = self.heroes.insert_one(hero)
        print(f"Héros '{name}' ajouté (ID: {result.inserted_id})")
        return result.inserted_id


class Game:
    def __init__(self, db_handler):
        self.db = db_handler

    def run(self):
        while True:
            self.show_main_menu()
            if not self.handle_main_choice():
                break

    def show_main_menu(self):
        print("\n========== Menu Principal ==========")
        print("1. Jouer")
        print("2. Ajouter un héros")
        print("3. Ajouter un monstre")
        print("4. Sauvegarder")
        print("5. Quitter")

    def handle_main_choice(self):
        choix = input("Choisissez une option: ").strip()

        if choix == '1':
            self.select_hero()
        elif choix == '2':
            self.create_hero()
        elif choix == '3':
            self.create_monster()
        elif choix == '4':
            print("Fonction de sauvegarde à implémenter...")
        elif choix == '5':
            print("Quitter le jeu.")
            return False
        else:
            print("Option invalide. Veuillez réessayer.")
        return True

    def select_hero(self):
        print("\n=== Liste des héros ===")
        for h in self.db.heroes.find():
            print(f"- {h['name']} (ATK: {h['ATK']}, DEF: {h['DEF']}, PV: {h['PV']})")

        choix_hero = input("Nom du héros choisi: ").strip()
        hero = self.db.heroes.find_one({'name': choix_hero})

        if hero:
            print(f"Vous avez choisi {hero['name']} (ATK {hero['ATK']}, DEF {hero['DEF']}, PV {hero['PV']}).")
            self.start_combat()
        else:
            print("Héros introuvable.")

    def create_hero(self):
        print("\n=== Ajout d’un nouveau héros ===")
        name = input("Nom : ")
        atk = int(input("ATK : "))
        defense = int(input("DEF : "))
        pv = int(input("PV : "))
        self.db.add_hero(name, atk, defense, pv)

    def create_monster(self):
        print("\n=== Ajout d’un nouveau monstre ===")
        name = input("Nom : ")
        atk = int(input("ATK : "))
        defense = int(input("DEF : "))
        pv = int(input("PV : "))
        self.db.add_monster(name, atk, defense, pv)

    def start_combat(self):
        print("\n=== Liste des ennemis disponibles ===")
        for m in self.db.monsters.find():
            print(f"- {m['name']} (ATK: {m['ATK']}, DEF: {m['DEF']}, PV: {m['PV']})")

        print("\n=== Menu de combat ===")
        print("1. Attaquer")
        print("2. Fuir")
        print("3. Quitter le jeu")

        choix = input("Choisissez une option: ").strip()
        if choix == '1':
            for m in self.db.monsters.find():
                print(f"{m['name']} attaque !")
        elif choix == '2':
            print("Vous fuyez le combat...")
        elif choix == '3':
            print("Fin du jeu.")
            exit()
        else:
            print("Choix invalide.")

