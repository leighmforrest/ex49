from ex49.character import Player
from ex49.engine import Engine
from ex49.map import Map
from ex49.scenes import GAME_ROOMS, ROOM_ADJACENCY


def init_player():
    while True:
        print("Please enter your player's name.")
        player_name = input("> ")

        if player_name:
            player = Player(player_name)
            return player
        else:
            continue


if __name__ == "__main__":
    print("Welcome to Dark Castle")

    player = init_player()

    map = Map(GAME_ROOMS, ROOM_ADJACENCY)
    engine = Engine(player, map, "dukes_chamber_1")
    engine.play()
