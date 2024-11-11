import random

from ex49.scene import Scene
from ex49.character import Character
from ex49.utilities import filtered_input, death


class DukesChamber1(Scene):
    def enter(self, player):
        print("DUKES' CHAMBER")
        # array of knights
        knights = [Character(f"Knight {i}", 7, 7) for i in range(6)]
        elixir = True 

        while knights:
            # knight always attacks
            knights[0].attack(player)
            if not player.is_alive():
                death("Your head has been sliced by the knight's halberd.")
            
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
    def enter(self, player):
        print("DUKE IS IN THE HOUSE!")

        duke = Character("The Duke", 20, 10)
        user_inputs = ["drink elixir", "attack", "pass"]
        golden_key = True

        while True:
            # Duke attacks first
            duke.attack(player)
            if not player.is_alive():
                death("You head has been sliced by the giant axe.")
            
            print("What do you do?")
            move = filtered_input(user_inputs)

            if "drink elixir":
                if "elixir" in player.inventory:
                    print("You have topped up your stamina.\n")
                    player.hp = 50
                    player.use_item("elixir")
                elif "attack":
                    player.attack(duke)
                    if not duke.is_alive():
                        print(f"{duke.name} has been defeated.")
                        break
                    
                    print(f"{player.name} stamina is {player.hp}")
                elif "pass":
                    continue
            
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
                return "treasure_room"
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

    def enter(self, player):
        print("SPIDER ROOM")

        while self.spiders:
            random.shuffle(self.spiders)
            print(f"There are {len(self.spiders)} spiders in the room.")
            # top spider always attacks
            self.spiders[0].attack(player)
            if not player.is_alive():
                death("Spider has sucked your gizzards through its chelicerae.")
            
            print("What do you do?")
            move = filtered_input(["attack", "pass"])

            if move == "attack":
                player.attack(self.spiders[0])
                if not self.spiders[0].is_alive():
                    print(f"{self.spiders[0].name} has been defeated.")
                    self.spiders.pop(0)
                print(f"{player.name} stamina is {player.hp}")
            if move == "pass":
                continue
        
        print("The spiders have been defated. Two doors appear ahead.")

        while True:
            if self.stink_bomb:
                print("The stink bomb appears where the spiders once stood.")
            
            print("What do you do now?")
            move = filtered_input(["take stink bomb", "door one", "door two"])

            if move == "door one":
                death("Large boulders roll, crushing you underneath.")
            elif move == "door two":
                return "wizards_lab"
            elif move == "take stink bomb":
                if self.stink_bomb:
                    player.new_item("stink_bomb")
                    self.stink_bomb = False
                else:
                    print("You already have the stink bomb.")
    

class WizardsLab(Scene):
    wizard_bombed = False
    grimoire = True

    def enter(self, player):
        choices_1 = ["attack", "throw bomb", "go back"]
        choices_2 = ["take grimoire", "open_door", "go back"]

        print("WIZARD'S LAB")

        while True:
            print("What action will you take?")
            move = filtered_input(choices_1)

            if move == "attack":
                if self.wizard_bombed:
                    print("There is no wizard to attack.")
                else:
                    death("Lightning bolts strike upon your head.")
            if move == "throw bomb":
                if "stink_bomb" in player.inventory and not self.wizard_bombed:
                    self.wizard_bombed = True
                    print("The wizard evacuates the laboratory.")
                    break
                else:
                    print("Cannot stink bomb the lab.")
            if move == "go back":
                return "spider_room"

        while True:
            if self.grimoire:
                print("The gilt grimoire is on the stand.")

            print("What do you do now?")
            move = filtered_input(choices_2)

            if move == "open door":
                death("Large boulders roll, crushing you underneath.")
            elif move == "go back":
                return "spider_room"
            elif move == "take grimoire":
                if self.grimoire:
                    player.new_item("grimoire")
                    self.grimoire = False
                else:
                    print("You already have the grimoire.")


class TreasureRoom(Scene):
    def enter(self, player):
        print("TREASURE ROOM")
        exit(0)