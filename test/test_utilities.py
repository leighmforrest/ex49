from unittest.mock import patch

from ex49.utilities import death, filtered_input


def test_filtered_input_valid_choice(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    allowed_values = (1, 2, 3, 4, 5)
    result = filtered_input(allowed_values, int)
    assert result == 3


def test_filtered_input_invalid_then_valid_choice(monkeypatch):
    inputs = iter(["6", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    allowed_values = (1, 2, 3, 4, 5)
    result = filtered_input(allowed_values, int)
    assert result == 2


def test_filtered_input_invalid_input_choice(monkeypatch):
    inputs = iter(["green", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    allowed_values = (1, 2, 3, 4, 5)
    result = filtered_input(allowed_values, int)
    assert result == 2


def test_filtered_input_invalid_input_choice_error_message(monkeypatch, capsys):
    inputs = iter(["green", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    allowed_values = (1, 2, 3, 4, 5)
    filtered_input(allowed_values, int)

    captured = capsys.readouterr()

    assert "Invalid input. Try again." in captured.out


def test_death():
    with patch("builtins.print") as mock_print:
        try:
            death("You have been defeated")
        except SystemExit as e:
            # Verify that the print function was called with the expected message
            mock_print.assert_called_once_with("You have been defeated", "GAME OVER.")

            assert e.code == 1
