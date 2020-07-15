# TEST DRIVEN ENVIRONMENT
# Import the file
import pytest
from scrabble import ScrabbleGame
my_scrabble_game = ScrabbleGame()


# Test file
# We need an iterative method to calculate the score
# A list of the scores

# test_list = {"dialogue", "grass", "nomination", "low", "disgrace"}

def test_scrabble_score_1():
    assert my_scrabble_game.scrabblescore("dog") == 5

def test_scrabble_score_2():
    assert my_scrabble_game.scrabblescore("cat") == 5

def test_scrabble_score_3():
    assert my_scrabble_game.scrabblescore("hello") == 8

def test_scrabble_score_4():
    assert my_scrabble_game.scrabblescore("low") == 6

def test_scrabble_score_5():
    assert my_scrabble_game.scrabblescore("testing") == 8

def test_scrabble_score_6():
    assert my_scrabble_game.scrabblescore("") == 0

# Write unit tests first!

# Class!

# Scrabble score calculator done
# Return the score for a word according to scrabble letter points done
# Randomly generate 7 tile hand
# Check that the word can be made using those tiles
# Once a word has been made, replace used tiles