from hangman_words import word_list
import random

# We want to create a class that contains the brains of the
# Hangman game

# We want to import the random word
# Apply any necessary transformations
# Preset the amount of tries - Keep this hidden
# When dealing with guesses
# If the guess is in the word then edit the list

# Select a random word from the word list
class Brain:

    def __init__(self):  # Initialisation (runs on instantiation)
        self.__word = random.choice(word_list)
        self.length = len(self.__word)

    def word_list(self):
        return list(self.__word)

    def get_word(self):
        return self.__word.lower()


winning_word = Brain()
