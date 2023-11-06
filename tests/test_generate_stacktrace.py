import pytest
import sys
import os
# Get the path of the current directory (where your test script is located)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Calculate the path to the src directory
src_directory = os.path.join(current_directory, '..', 'src')

# Add the src directory to sys.path
sys.path.append(src_directory)


# test_generate_stacktrace.py
from pyprankerror import generate_stacktrace, short, long, shortfunny, longfunny  # Import the function you want to test

def test_generate_stacktrace_short(capsys):
    generate_stacktrace(length=0, is_silly=False)
    captured = capsys.readouterr()
    assert captured.out == short
    
def test_generate_stacktrace_long(capsys):
    generate_stacktrace(length=0, is_silly=False)
    captured = capsys.readouterr()
    assert captured.out == long
    
def test_generate_stacktrace_shortfunny(capsys):
    generate_stacktrace(length=0, is_silly=False)
    captured = capsys.readouterr()
    assert captured.out == shortfunny
    
def test_generate_stacktrace_longfunny(capsys):
    generate_stacktrace(length=0, is_silly=False)
    captured = capsys.readouterr()
    assert captured.out == longfunny
