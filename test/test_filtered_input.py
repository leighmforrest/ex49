import pytest
from ex49.filtered_input import filtered_input


def test_filtered_input_valid_choice(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    allowed_values = (1,2,3,4,5)
    result = filtered_input(allowed_values, int)
    assert result == 3


def test_filtered_input_invalid_then_valid_choice(monkeypatch):
    inputs = iter(["6", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    allowed_values = (1,2,3,4,5)
    result = filtered_input(allowed_values, int)
    assert result == 2


def test_filtered_input_invalid_input_choice(monkeypatch):
    inputs = iter(["green", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    allowed_values = (1,2,3,4,5)
    result = filtered_input(allowed_values, int)
    assert result == 2


def test_filtered_input_invalid_input_choice_error_message(monkeypatch, capsys):
    # Simulate user input: first "green" (invalid), then "2" (valid)
    inputs = iter(["green", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    allowed_values = (1, 2, 3, 4, 5)
    filtered_input(allowed_values, int)
    
    # Capture output after the function has run
    captured = capsys.readouterr()
    
    # Check that the function printed the correct error message
    assert "Invalid input. Try again." in captured.out
