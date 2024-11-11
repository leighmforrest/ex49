from ex49.scenes.rooms import (
    DukesChamber1,
    DukesChamber2,
    Sphinx,
    SpiderRoom,
    TreasureRoom,
    WizardsLab,
    MephistopholesLair
)

GAME_ROOMS = {
    "dukes_chamber_1": DukesChamber1(),
    "dukes_chamber_2": DukesChamber2(),
    "spider_room": SpiderRoom(),
    "wizards_lab": WizardsLab(),
    "sphinx": Sphinx(),
    "mephistopholes_lair": MephistopholesLair(),
    "treasure_room": TreasureRoom(),
}


ROOM_ADJACENCY = {
    "dukes_chamber_1": ["dukes_chamber_2"],
    "dukes_chamber_2": ["spider_room"],
    "spider_room": ["wizards_lab", "sphinx"],
    "wizards_lab": ["mephistopholes_liar", "spider_room"],
    "mephistopholes_lair": ["treasure_room"],
    "sphinx": ["spider_room"],
}
