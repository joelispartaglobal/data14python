from scrabble import ScrabbleGame
my_scrabble_game = ScrabbleGame()


def test_scrabble_score_1():
    assert my_scrabble_game.scrabblescore("dog") == 5

def test_scrabble_score_2():
    assert my_scrabble_game.scrabblescore("cat") == 5

def test_scrabble_score_3():
    assert my_scrabble_game.scrabblescore("hello") == 8

def test_scrabble_score_4():
    assert my_scrabble_game.scrabblescore("something") != 0

def test_scrabble_score_5():
    assert my_scrabble_game.scrabblescore("hello") != 23123

def test_scrabble_score_6():
    assert my_scrabble_game.scrabblescore("cat") != 2

def test_tile_generation():
    assert len(my_scrabble_game.tilegeneration()) == 7

def test_tile_generation_2():
    assert len(my_scrabble_game.tilegeneration()) != 6

def test_tile_generation_3():
    assert len(my_scrabble_game.tilegeneration()) != 8

# Class!

# Scrabble score calculator done
# Return the score for a word according to scrabble letter points done
# Randomly generate 7 tile hand done
# Check that the word can be made using those tiles still need doing
# Once a word has been made, replace used tiles still need doing