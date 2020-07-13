from hangman_words import word_list
import random

reattempt = True
while reattempt:
    # Select a random word from the word list
    random_choice = random.choice(word_list)

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
        print(underscore)
    else:
        print("Goodbye")
        break

    # 2) It will tell you to guess a letter
    # 3a) If it is correct, it will replace an underscore with the appropriate letter

    # Create a list for guessed and incorrect
    guess = []

    while tries > 0:
        guess = input("Please guess a letter. \n")
        out = ''
        if guess.lower() in random_word.lower():
            print("Good job")
            out += guess
            print(out)
        else:
            print("Incorrect, try again")
            print(f"You have {tries - 1} tries left")
            out += underscore
            print(out + underscore)
            tries -= 1

        if out.lower() == random_word.lower():
            print("Congratulations, you have guessed correctly!")
            print("The word is:")
            print(out)

    if tries == 0:
        print("Game over, do you want to try again?")
        reattempt = input("Type Yes/No \n")
        if reattempt.lower() == "yes":
            reattempt = True
        else:
            print("Goodbye")
            reattempt = False

# 3b) If it is wrong, you will get a message and one part of the hangman will be drawn
# When one of two conditions have been met done
# 4a) Successfully completed the word, you will be congratulated and asks if you want to play again
# 4b) Failed, and asks you if you want to play again