from ex49.scenes.rooms import DukesChamber1, DukesChamber2, SpiderRoom, TreasureRoom

GAME_ROOMS = {
    "dukes_chamber_1": DukesChamber1(),
    "dukes_chamber_2": DukesChamber2(),
    "spider_room": SpiderRoom(),
    "treasure_room": TreasureRoom()
}


ROOM_ADJACENCY = {
    "dukes_chamber_1": ["dukes_chamber_2"],
    "dukes_chamber_2": ["spider_room"],
    "spider_room": ["treasure_room"],
}