# import random as rand
# from classes import Dog
#
# print(rand.randint(0,6))
#
# my_list = [1, 2, 3, 4, 5, 6]
#
# print(rand.choice(my_list))
#
# new_dog = Dog("Fido")
# print(new_dog.intro())

from hangman_words import word_list
import random

# Select a random word from the word list
random_word = random.choice(word_list)

# Preload the length of the word
word_len = len(random_word)

# Create the amount of underscores based on the length of the word
underscore = '_' * word_len

# How many chances of getting it wrong

# We want to create a class where

# 1) It initiates the game
print("Welcome to Hangman!")
confirm = input("Do you want to roll again? Type either 'yes' or 'no' ")

if confirm.lower() == "yes":
    # Guess the word
    print("Here is your word to guess")
    print(underscore)
else:
    print("Goodbye")

# 2) It will tell you to guess a letter
# 3a) If it is correct, it will replace an underscore with the appropriate letter
# 3b) If it is wrong, you will get a message and one part of the hangman will be drawn

# When one of two conditions have been met
# 4a) Successfully completed the word, you will be congratulated and asks if you want to play again
# 4b) Failed, and asks you if you want to play again