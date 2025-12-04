from pymongo import MongoClient
from bson.objectid import ObjectId
from game import Game
from game import hero
from game import client

if __name__ == "__main__":
    game = Game(hero)
    game.run()
    client.close()