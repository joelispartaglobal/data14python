import brain_class as bc
# Import word from brain class
chosen_word = bc.chosen_word.get_word()

class Game:

    # Initialise method to welcome the user
    def __init__(self):
        self.tries = 7
        self.reattempt = True
        self.underscore = ''
        print(chosen_word)
        print("Welcome to Hangman!")

    # Method to ask the user to confirm if they want to play
    def play(self):
        confirm = input("Do you want to play? Type either 'yes' or 'no' ")

        if confirm.lower() == "yes":
            # Guess the word
            print("Here is your word to guess")
            print(len(chosen_word) * "_")
        else:
            print("Goodbye")

    # Turn underscore into a list so it can be compared to
    def underscore_list(self):
        return list(self.underscore)

    # Main body of the game
    # Method to find occurrences letters

    def findoccurrences(self, s, ch):
        return [i for i, letter in enumerate(s) if letter == ch]

    # Hangman game
    def hangman_guess(self):
        while self.tries > 0:
            guess = input("Please guess a letter. \n")
            if 0 < len(guess) > 1:
                print("Stop cheating")
            elif guess.isnumeric():
                print("Please do not guess numbers")
            elif guess.lower() in chosen_word:

                # If correct guess
                # Find where the letter occurs in the word]
                print("Good job, you guessed a letter correctly")
                index = self.findoccurrences(chosen_word, guess)
                underscore = list(chosen_word)
                for i in index:
                    underscore[i] = guess
                print(underscore)

    # Create a method to subtract a try if they guessed wrong
    def subtract_try(self):
        # If guess is incorrect
        # Minus one try from tries
        print("Incorrect, try again")
        print(f"You have {self.tries - 1} tries left")
        self.tries -= 1

    # Create a method if the guess is incorrect
    def hangman_wrong(self):
        print("Incorrect, try again")
        print(f"You have {self.tries - 1} tries left")
        self.tries -= 1

    # Create a method to congratulate the user for guessing correctly
    def congrats(self):
        while self.tries > 0:
            if self.underscore == chosen_word:
                print("Congratulations, you have guessed correctly!")
                print("The word is:")
                print(chosen_word.upper())

    # Create a method to allow the user to restart the game
    def restart_game(self):
        print("Do you want to play again?")
        reattempt = input("Type Yes/No \n")
        if reattempt.lower() == "yes":
            self.reattempt = True
        else:
            print("Goodbye")
            self.reattempt = False

    # Create a method

try_game = Game()
try_game.hangman_guess()