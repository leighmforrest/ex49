import pytest
from unittest.mock import patch


def test_engine_is_none(engine):
    assert len(engine.scene_map.scenes) == 3


def test_run_game(engine):
    with patch("builtins.print") as mock_print:
        try:
            engine.play()
        except SystemExit as e:
            mock_print.assert_called_with("YOU WIN")
            assert e.code == 0


def test_engine_fail_adjacent(bad_engine):
    with pytest.raises(ValueError) as excinfo:
        bad_engine.play()
    # Assert the exception message is as expected.
    assert str(excinfo.value) == "Next scene is not adjacent to current scene."