from unittest.mock import patch

import pytest

from ex49.character import ITEMS, WEAPONS

BAD_ITEMS = ("Model 29", "slingshot", "blue")


def test_character_exists(character):
    assert character.name == "Ganon"
    assert character.hp > 0
    assert character.max_attack > 0
    assert character is not None


def test_character_no_negative_hp(character):
    new_hp = character.hp + 2
    character.hp -= new_hp
    assert character.hp == 0


def test_character_is_alive(character):
    new_hp = character.hp + 2
    character.hp -= new_hp
    assert not character.is_alive()


def test_character_attack_repelled(character, opponent, capsys):
    with patch("random.randint", return_value=0):
        character.attack(opponent)
        captured = capsys.readouterr()

    assert opponent.hp == 1
    assert opponent.is_alive() is True
    assert f"The attack on {opponent.name} has been repelled." in captured.out


def test_character_direct_hit(character, opponent, capsys):
    with patch("random.randint", return_value=2):
        character.attack(opponent)
        captured = capsys.readouterr()

    assert opponent.hp == 0
    assert opponent.is_alive() is False
    f"{character.name} attacks {opponent.name} for" in captured.out


def test___str__self(character):
    assert str(character) == f"{character.name}: {character.hp}"


def test_player(player):
    assert player is not None
    assert player.name == "Link"
    assert player.hp == 50
    assert player.weapon == "dagger"
    assert player.max_attack == WEAPONS[player.weapon]


def test_player_new_weapon(player):
    player.new_weapon("sword")
    assert player.weapon == "sword"
    assert player.max_attack == WEAPONS["sword"]


def test_player_new_weapon_fail(player, capsys):
    player.new_weapon("shovel")
    captured = capsys.readouterr()

    assert "Weapon not found" in captured.out
    assert player.weapon != "shovel"


@pytest.mark.parametrize("item", ITEMS)
def test_new_item_success(player, item):
    player.new_item(item)

    assert item in player.inventory


@pytest.mark.parametrize("item", BAD_ITEMS)
def test_new_item_failure(capsys, player, item):
    player.new_item(item)
    captured = capsys.readouterr()

    assert item not in player.inventory
    assert "Item not found" in captured.out


@pytest.mark.parametrize("item", ITEMS)
def test_use_item_success(player, item):
    player.new_item(item)
    player.use_item(item)

    assert item not in player.inventory


@pytest.mark.parametrize("item", ITEMS)
def test_use_item_success(player, item):
    player.new_item(item)
    player.use_item(item)

    assert item not in player.inventory


@pytest.mark.parametrize("item,bad_item", zip(ITEMS, BAD_ITEMS))
def test_use_item_failure(player, item, bad_item):
    print(item, bad_item)
    player.new_item(item)
    player.use_item(bad_item)

    assert bad_item not in player.inventory
