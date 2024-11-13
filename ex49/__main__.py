import sys

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
    starting_room = "dukes_chamber_1"

    player = init_player()
    args = len(sys.argv)

    if args == 2:
        cheat_code = sys.argv[1]

        if cheat_code == "nrcczbitzohxzmzcphbruagxa":
            player.new_item("elixir")
            player.new_item("grimoire")
            player.new_weapon("sword")
            starting_room = "mephistopheles_lair"
        elif cheat_code == "lxvjdpoqupeeufrpenlpikzal":
            player.new_item("golden key")
            starting_room = "spider_room"
        else:
            print("Cheat code is unknown. Start from beginning...")

    map = Map(GAME_ROOMS, ROOM_ADJACENCY)
    engine = Engine(player, map, "mephistopheles_lair")
    engine.play()
