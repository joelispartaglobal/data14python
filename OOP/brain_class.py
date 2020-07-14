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
        self._random_choice = random.choice(word_list).lower()

    def random_choice_list(self):
        self._random_choice = random.choice(word_list).lower()
        return list(self._random_choice)

    # def word(self):
    #     random_word = self._random_choice
    #
    # # Preload the length of the word
    # def word_length(self):
    #     word_len = len(self._random_word)
    #
    # # Create the amount of underscores based on the length of the word
    # def underscore_len():
    #     underscore = '_' * self.word_len
    #     print(self_.random_word)  # Remember to delete this


print(Brain.random_choice_list)