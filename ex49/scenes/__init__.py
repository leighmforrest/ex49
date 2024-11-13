from ex49.scenes.rooms import (
    DukesChamber1,
    DukesChamber2,
    MephistopholesLair,
    Sphinx,
    SpiderRoom,
    TreasureRoom,
    WizardsLab,
)

GAME_ROOMS = {
    "dukes_chamber_1": DukesChamber1(),
    "dukes_chamber_2": DukesChamber2(),
    "spider_room": SpiderRoom(),
    "wizards_lab": WizardsLab(),
    "sphinx": Sphinx(),
    "mephistopheles_lair": MephistopholesLair(),
    "treasure_room": TreasureRoom(),
}


ROOM_ADJACENCY = {
    "dukes_chamber_1": ["dukes_chamber_2"],
    "dukes_chamber_2": ["spider_room"],
    "spider_room": ["wizards_lab", "sphinx"],
    "wizards_lab": ["mephistopheles_lair", "spider_room"],
    "mephistopheles_lair": ["treasure_room"],
    "sphinx": ["spider_room"],
}
