import pytest

from ex49.map import Map
from ex49.scene import Scene


def test_map____init___success(map):
    assert isinstance(map, Map)
    assert len(map.scenes) == 3
    assert len(map.adjacent_scenes) == 2


def test_map___init___fail():
    with pytest.raises(ValueError) as e:
        Map([], [])
        assert str(e.value) == "Arguments must be dictionaries."


def test_map_scenes_setter(map):
    map.scenes = {}
    assert map.scenes == {}


def test_map_scenes_setter_fail(map):
    with pytest.raises(ValueError) as e:
        map.scenes = []
        assert str(e.value) == "Scenes must be a dictionary."


def test_map_adjacent_scenes_setter(map):
    map.adjacent_scenes = {}
    assert map.adjacent_scenes == {}


def test_map_adjacent_scenes_setter_fail(map):
    with pytest.raises(ValueError) as e:
        map.adjacent_scenes = []
        assert str(e.value) == "Adjacent scenes must be a dictionary."


@pytest.mark.parametrize(
    "scene,adjacents",
    [("atrium", ["green"]), ("green", ["finished", "atrium"]), ("red", None)],
)
def test_get_next_scenes(scene, adjacents, map):
    assert map.get_next_scenes(scene) == adjacents


@pytest.mark.parametrize("scene", ["atrium", "green", "finished"])
def test_get_scene(scene, map):
    returned_scene = map.get_scene(scene)
    assert isinstance(returned_scene, Scene)


@pytest.mark.parametrize("scene", ["red", "cyan", "magenta"])
def test_get_scene_fail(scene, map):
    returned_scene = map.get_scene(scene)
    assert returned_scene is None
