from pymongo import MongoClient
from bson.objectid import ObjectId

def Menu():
    print("\nMenu :\n"
        "1. Choisir un Hero\n"
        "2. Historique de partie\n"
        "3. Quitter\n"
    )