import pytest

from ex49.character import Character, Player
from ex49.map import Map
from test.scenes_for_testing import SCENES, ADJACENT_SCENES


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