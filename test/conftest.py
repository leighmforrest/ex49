import pytest

from ex49.character import Character, Player


@pytest.fixture
def character():
    return Character("Ganon", 10, 10)


@pytest.fixture
def opponent():
    return Character("Barry Horowitz", 1, 1)


@pytest.fixture
def player():
    return Player("Link")