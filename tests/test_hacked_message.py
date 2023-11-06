import pytest
from unittest.mock import patch
import sys
import os

# Get the path of the current directory (where your test script is located)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Calculate the path to the src directory
src_directory = os.path.join(current_directory, '..', 'src')

# Add the src directory to sys.path
sys.path.append(src_directory)

from pyprankerror import generate_hacked_message

# --------------- Hacked Message Test Code ---------------------
@pytest.fixture
def mock_random_choice():
    with patch('random.choice') as mock:
        yield mock

def test_default_arguments(mock_random_choice, capsys):
    mock_random_choice.return_value = "potato"
    generate_hacked_message()
    captured = capsys.readouterr()
    assert "Your computer has been hacked by a potato." in captured.out

def test_is_silly_true(mock_random_choice, capsys):
    mock_random_choice.return_value = "robot"
    generate_hacked_message(is_silly=True)
    captured = capsys.readouterr()
    assert "Your computer has been hacked by a robot." in captured.out

def test_length_of_output(mock_random_choice, capsys):
    mock_random_choice.return_value = "friendly alien"
    generate_hacked_message(length_of_output=3)
    captured = capsys.readouterr()
    assert "Your computer has been hacked by a friendly alien." in captured.out
    assert "Hacking ID:" in captured.out

def test_length_of_output_and_silly_true(mock_random_choice, capsys):
    mock_random_choice.return_value = "unicorn"
    generate_hacked_message(length_of_output=2, is_silly=True)
    captured = capsys.readouterr()
    assert "Your computer has been hacked by a unicorn." in captured.out
    assert "Hacked by:" in captured.out
    assert "Hacking ID:" in captured.out
# --------------- End of Hacked Message Test Code ---------------------
