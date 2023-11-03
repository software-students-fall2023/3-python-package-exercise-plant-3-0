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

from crash import generate_crash_report, silly_long, silly_short, long, short

# --------------- Crash Report Test Code ---------------------
@pytest.fixture
def mock_random_randint():
    with patch('random.randint') as mock:
        yield mock

def test_default_arguments(mock_random_randint, capsys):
    mock_random_randint.return_value = 2
    generate_crash_report()
    captured = capsys.readouterr()
    assert captured.out.strip() == short[2]

def test_is_long_true(mock_random_randint, capsys):
    mock_random_randint.return_value = 3
    generate_crash_report(is_long=True)
    captured = capsys.readouterr()
    assert captured.out.strip() == long[3]

def test_is_silly_true(mock_random_randint, capsys):
    mock_random_randint.return_value = 1
    generate_crash_report(is_silly=True)
    captured = capsys.readouterr()
    assert captured.out.strip() == silly_short

def test_is_long_and_silly_true(mock_random_randint, capsys):
    mock_random_randint.return_value = 0
    generate_crash_report(is_long=True, is_silly=True)
    captured = capsys.readouterr()
    assert captured.out.strip() == silly_long
# --------------- End of Crash Report Test Code ---------------------

