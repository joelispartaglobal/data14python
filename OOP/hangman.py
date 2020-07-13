from hangman_words import word_list
import random

# Select a random word from the word list
random_word = random.choice(word_list)

# Preload the length of the word
word_len = len(random_word)

# Create the amount of underscores based on the length of the word
underscore = '_' * word_len

# How many chances of getting it correct

tries = 7

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

guess = input("Please guess a letter. \n")

# 3a) If it is correct, it will replace an underscore with the appropriate letter

while tries > 0:

    if guess in random_word:
        print("Good job")
    else:
        print("Incorrect, try again")
        tries -= 1

# 3b) If it is wrong, you will get a message and one part of the hangman will be drawn



# When one of two conditions have been met
# 4a) Successfully completed the word, you will be congratulated and asks if you want to play again
# 4b) Failed, and asks you if you want to play again