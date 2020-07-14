import brain_class as bc
# Import word from brain class
from hangman import guess

chosen_word = bc.chosen_word.get_word()

class Game:
    # Initialise method to welcome the user
    tries = 7
    guess = []

    def __init__(self):
        print(chosen_word)  # Remember to delete
        print("Hello there \n")
        self.reattempt = ''
        self._underscore = ''
        self._confirm = ''
        self.chosen_word = bc.chosen_word.get_word()
        self.play()
        self.hangman_guess()
        self.congrats()
        self.fail()
        # self.congrats()

    def start(self):
        print("something")
        self.play()

    # Method to ask the user to confirm if they want to play
    def play(self):
        self._confirm = input("Do you want to play? Type either 'yes' or 'no' ")
        if self._confirm.lower() == "yes":
            # Guess the word
            print("Here is your word to guess")
            print(len(chosen_word) * "_")
        else:
            print("Goodbye")

    # Turn underscore into a list so it can be compared to
    def underscore_list(self):
        return list(self._underscore)

    # Main body of the game
    # Method to find occurrences letters
    def findoccurrences(self, s, ch):
        return [i for i, letter in enumerate(s) if letter == ch]

    # Hangman game
    def hangman_guess(self):
        if self._confirm.lower() == "yes":
            while self.tries > 0:
                guess_input = input("Please guess a letter. \n")
                if 0 < len(guess_input) > 1:
                    print("Stop cheating")
                elif guess_input.isnumeric():
                    print("Please do not guess numbers")
                # If we guess the letter correctly
                if guess_input in chosen_word.lower():
                    print("Good job, you guessed a letter correctly")
                    guess.append(guess_input)
                    index = self.findoccurrences(chosen_word, guess)
                    self._underscore = list(chosen_word)
                    for i in index:
                        self._underscore[i] = chosen_word
                        print(self._underscore)
                else:
                    print("Incorrect, try again \n")
                    print(f"You have {self.tries - 1} tries left")
                    self.tries -= 1

    # Create a method to congratulate the user for guessing correctly
    def congrats(self):
        if self.tries > 0:
            if self.guess == chosen_word:
                print("Congratulations, you have guessed correctly!")
                print("The word is:")
                print(chosen_word.upper())

    def fail(self):
        if self.tries == 0:
            print("You have lost. \n Goodbye.")

    # # Create a method to allow the user to restart the game
    # def restart_game(self):
    #     print("Do you want to play again?")
    #     reattempt = input("Type Yes/No \n")
    #     if reattempt.lower() == "yes":
    #         self.reattempt = True
    #     else:
    #         print("Goodbye")
    #         self.reattempt = False


try_game = Game()

