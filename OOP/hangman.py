from hangman_words import word_list
import random

# Function so that if we guess a letter correctly, it will place that letter in the
# Respective place in the list
def findoccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

# Reattempt allows the game to be played in a loop
reattempt = True
while reattempt:

    # Select a random word from the word list
    random_choice = random.choice(word_list).lower()
    random_choice_list = list(random_choice)
    random_word = random_choice

    # Preload the length of the word
    word_len = len(random_word)

    # Create the amount of underscores based on the length of the word
    underscore = '_' * word_len
    print(random_word)   # Remember to delete this

    # How many chances of getting it correct
    tries = 7

    # We want to create a class where
    # 1) It initiates the game
    print("Welcome to Hangman!")
    confirm = input("Do you want to play? Type either 'yes' or 'no' ")

    if confirm.lower() == "yes":
        # Guess the word
        print("Here is your word to guess")
        print(list(underscore))
    else:
        print("Goodbye")
        break

    # Create an empty string for the answer
    answer = ''

    # Hangman game in while loop
    while tries > 0:

        guess = input("Please guess a letter. \n")
        if 0 < len(guess) > 1:
            print("Stop cheating")
        elif guess.isnumeric():
            print("Please do not guess numbers")
        elif guess.lower() in random_word.lower():
            # If correct guess
            # Find where the letter occurs in the word
            print("Good job, you guessed a letter correctly")
            index = findoccurrences(random_choice_list, guess)
            underscore = list(underscore)
            for i in index:
                underscore[i] = guess
            print(underscore)
        else:
            # If guess is incorrect
            # Minus one try from tries

            print("Incorrect, try again")
            print(f"You have {tries - 1} tries left")
            tries -= 1

        # When guessed correctly display the word
        # Enquire if they want to play again

        if underscore == random_choice_list:
            print("Congratulations, you have guessed correctly!")
            print("The word is:")
            print(random_word.upper())
            print("Do you want to play again?")
            reattempt = input("Type Yes/No \n")
            if reattempt.lower() == "yes":
                reattempt = True
                break
            else:
                print("Goodbye")
                reattempt = False
                break
    # If game over
    # Do they want to reattempt
    if tries == 0:
        print("Game over, do you want to try again?")
        reattempt = input("Type Yes/No \n")
        if reattempt.lower() == "yes":
            reattempt = True
        else:
            print("Goodbye")
            reattempt = False
