from ex49.character import Player


def init_player():
    while True:
        print("Please enter your player's name.")
        player_name = input("> ")
        
        if player_name:
            player = Player(player_name)
            return player
        else: continue


if __name__ == "__main__":
    print("Welcome to Monster Maze")

    from ex49.character import Player

if __name__ == "__main__":
    print("Welcome to Monster Maze")
    player = init_player()
    print(player)