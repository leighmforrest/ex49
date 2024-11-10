from ex49.character import Player
from ex49.scenes import GAME_ROOMS, ROOM_ADJACENCY
from ex49.engine import Engine
from ex49.map import Map


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
    print("Welcome to Monster Maze")
    player = init_player()
    print(player)

    map = Map(GAME_ROOMS, ROOM_ADJACENCY)
    engine = Engine(player, map, "spider_room")
    engine.play()
