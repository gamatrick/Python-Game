from game import Game
from game import DatabaseHandler

if __name__ == "__main__":
    db_handler = DatabaseHandler()
    db_handler.reset_collections()
    db_handler.init_data()

    game = Game(db_handler)
    game.run()