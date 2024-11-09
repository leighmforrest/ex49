from ex49.scene import Scene


class Atrium(Scene):
    def enter(self, player):
        return "green"


class Green(Scene):
    def enter(self, player):
        return "finished"


class Finished(Scene):
    def enter(self, player):
        print("YOU WIN")
        exit(0)


SCENES = {"atrium": Atrium(), "green": Green(), "finished": Finished()}

ADJACENT_SCENES = {"atrium": ["green"], "green": ["finished", "atrium"]}


BAD_ADJACENT_SCENES = {
    "atrium": [],
    "green": ["finished", "atrium"],
    "finished": [],
}
