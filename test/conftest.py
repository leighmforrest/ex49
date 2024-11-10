from test.scenes_for_testing import ADJACENT_SCENES, BAD_ADJACENT_SCENES, SCENES

import pytest

from ex49.character import Character, Player
from ex49.engine import Engine
from ex49.map import Map


@pytest.fixture
def character():
    return Character("Ganon", 10, 10)


@pytest.fixture
def opponent():
    return Character("Barry Horowitz", 1, 1)


@pytest.fixture
def player():
    return Player("Link")


@pytest.fixture
def map():
    return Map(SCENES, ADJACENT_SCENES)


@pytest.fixture
def engine(player, map):
    return Engine(player, map, "atrium")


@pytest.fixture
def bad_engine(player):
    map = Map(SCENES, BAD_ADJACENT_SCENES)
    return Engine(player, map, "atrium")
