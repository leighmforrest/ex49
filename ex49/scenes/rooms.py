import random

from ex49.character import Character
from ex49.scene import Scene
from ex49.scenes.dialogue import DIALOGUE
from ex49.utilities import death, filtered_input


class DukesChamber1(Scene):
    dialogue = DIALOGUE["dukes_chamber_1"]

    def enter(self, player):
        print(self.dialogue["description"])
        # array of knights
        knights = [Character(f"Knight {i}", 7, 7) for i in range(6)]
        elixir = True

        while knights:
            # knight always attacks
            knights[0].attack(player)
            if not player.is_alive():
                death(self.dialogue["death"])

            print("What do you do?")
            move = filtered_input(["attack", "pass"])

            if move == "attack":
                player.attack(knights[0])
                if not knights[0].is_alive():
                    print(f"{knights[0].name} has been defeated.")
                    knights.pop(0)
                print(f"{player.name} stamina is {player.hp}")
            if move == "pass":
                continue

        print(self.dialogue["victory"])

        while True:
            if elixir:
                print("There is a bottle of elixir at your foot.")

            print("What do you do now?")
            move = filtered_input(["take elixir", "advance"])

            if move == "advance":
                return "dukes_chamber_2"
            elif move == "take elixir":
                if elixir:
                    player.new_item("elixir")
                    elixir = False
                else:
                    print("You already have the elixir.")


class DukesChamber2(Scene):
    dialogue = DIALOGUE["dukes_chamber_2"]

    def enter(self, player):
        print(self.dialogue["description"])

        duke = Character("The Duke", 20, 10)
        user_inputs = ["drink elixir", "attack", "pass"]
        golden_key = True

        while True:
            # Duke attacks first
            duke.attack(player)
            if not player.is_alive():
                death(self.dialogue["death"])

            print("What do you do?")
            move = filtered_input(user_inputs)
            print("")

            if move == "drink elixir":
                if "elixir" in player.inventory:
                    print("You have topped up your stamina.\n")
                    player.hp = 50
                    player.use_item("elixir")
            elif move == "attack":
                player.attack(duke)
                if not duke.is_alive():
                    print(f"{duke.name} has been defeated.")
                    break

                print(f"{player.name} stamina is {player.hp}")
            elif move == "pass":
                continue

        print(self.dialogue["victory"])

        while True:
            if golden_key:
                print("The golden key is on the marble floor.")
            print("What is your next move?")
            move = filtered_input(["take key", "advance"])

            if move == "take key":
                if golden_key:
                    player.new_item("golden key")
                    golden_key = False
                else:
                    print("You have the golden key")
            elif move == "advance":
                return "spider_room"
            else:
                continue


class SpiderRoom(Scene):
    spiders = [
        Character("Spider 1", 7, 7),
        Character("Spider 2", 6, 6),
        Character("Spider 3", 5, 5),
        Character("Spider 4", 5, 5),
        Character("Spider 5", 4, 4),
        Character("Spider 6", 4, 4),
        Character("Spider 7", 4, 4),
    ]
    stink_bomb = True
    dialogue = DIALOGUE["spider_room"]

    def enter(self, player):
        print(self.dialogue["description"])

        while self.spiders:
            random.shuffle(self.spiders)

            n = len(self.spiders)

            if n > 1:
                spider_count = f"There are {n} spiders in the room."
            else:
                spider_count = "There is one spider in the room."
            print(spider_count)

            # top spider always attacks
            self.spiders[0].attack(player)
            if not player.is_alive():
                death(self.dialogue["death"])

            print("What do you do?")
            move = filtered_input(["attack", "pass"])

            if move == "attack":
                player.attack(self.spiders[0])
                if not self.spiders[0].is_alive():
                    print(f"{self.spiders[0].name} has been defeated.")
                    self.spiders.pop(0)
                print(f"{player.name} stamina is {player.hp}")
            elif move == "pass":
                continue

        # After defeating all spiders
        while True:
            print(self.dialogue["victory"])
            if self.stink_bomb:
                print("There is a stink bomb on the floor.")

            print("What do you do now?")
            move = filtered_input(["take stink bomb", "door one", "door two"])

            if move == "take stink bomb":
                if self.stink_bomb:
                    player.new_item("stink_bomb")
                    self.stink_bomb = False
                else:
                    print("You already have the stink bomb.")
            elif move == "door one":
                return "sphinx"
            elif move == "door two":
                return "wizards_lab"
            else:
                print("Invalid choice. Try again.")


class WizardsLab(Scene):
    wizard_bombed = False
    grimoire = True
    dialogue = DIALOGUE["wizards_lab"]

    def enter(self, player):
        choices_1 = ["attack", "throw bomb", "go back"]
        choices_2 = ["take grimoire", "open door", "go back"]

        print(self.dialogue["description"])

        if self.wizard_bombed:
            print(self.dialogue["wizard"])

        while not self.wizard_bombed:
            print("What action will you take?")
            move = filtered_input(choices_1)

            if move == "attack":
                if self.wizard_bombed:
                    print("There is no wizard to attack.")
                else:
                    death(self.dialogue["death"])
            if move == "throw bomb":
                if "stink_bomb" in player.inventory and not self.wizard_bombed:
                    self.wizard_bombed = True
                    print(self.dialogue["victory"])
                    break
                else:
                    print("Cannot stink bomb the lab.")
            if move == "go back":
                return "spider_room"

        while True:
            if self.grimoire:
                print("The gilt grimoire is on the stand.")

            print(f"Weapon: {player.weapon}")
            print(f"Inventory: {player.inventory}")
            print("What do you do now?")
            move = filtered_input(choices_2)

            if move == "go back":
                return "spider_room"
            elif move == "take grimoire":
                if self.grimoire:
                    player.new_item("grimoire")
                    self.grimoire = False
                else:
                    print("You already have the grimoire.")
            elif move == "open door":
                if player.weapon == "sword" and "golden key" in player.inventory:
                    return "mephistopholes_lair"
                else:
                    print(
                        "You must have the sword and the golden key to open the door."
                    )


class Sphinx(Scene):
    solved = False
    dialogue = DIALOGUE["sphinx"]

    def enter(self, player):
        max_guesses = 3
        answer = "time"

        if self.solved:
            print("You have already solved the riddle.")
        else:
            print(self.dialogue["description"])
            print(self.dialogue["sphinx_talk"])

            for _ in range(3):
                print("What is your answer?")
                guess = input("> ").lower()
                if guess == answer:
                    self.solved = True
                    break

            if self.solved:
                # issue sword
                player.new_weapon("sword")
                # issue elixir
                player.new_item("elixir")

                print(self.dialogue["riddle_solved"])

            else:
                death(self.dialogue["death"])

        # If solved, the user must enter go back.
        print("What is your next move?")
        filtered_input(["go back"])
        return "spider_room"


class MephistopholesLair(Scene):
    dialogue = DIALOGUE["mephistopheles_lair"]
    mephistopholes = Character("Mephistopholes", 76, 15)

    def enter(self, player):
        print(self.dialogue["description"])

        while self.mephistopholes.is_alive():
            self.mephistopholes.attack(player)
            if not player.is_alive():
                death(self.dialogue["death"])

            print("What do you do?")
            move = filtered_input(["attack", "pass", "drink elixir"])

            if move == "attack":
                player.attack(self.mephistopholes)
                if not self.mephistopholes.is_alive():
                    print(f"{self.mephistopholes.name} has been defeated.")

                print(f"{player.name} stamina is {player.hp}")

            elif move == "drink elixir":
                if "elixir" in player.inventory:
                    print("You have topped up your stamina.\n")
                    player.hp = 50
                    player.use_item("elixir")
                else:
                    print("You do not have elixir.")

            elif move == "pass":
                continue

        print(self.dialogue["victory"])
        return "treasure_room"


class TreasureRoom(Scene):
    def enter(self, player):
        print("TREASURE ROOM")
        exit(0)
