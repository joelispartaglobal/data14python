import brain_class as bc
# Import word from brain class

chosen_word = bc.chosen_word.get_word()

class Game:
    # Initialise method to welcome the user
    tries = 7
    guess = []

    def __init__(self):
        print(chosen_word)  # Remember to delete
        print("Hello! Welcome to hangman! \n")
        self.reattempt = ''
        self._underscore = list("_" * len(chosen_word))
        self._confirm = ''
        self.underscore_list()
        self.chosen_word = bc.chosen_word.get_word()
        self.play()
        self.hangman_guess()
        self.fail()

    # Method to ask the user to confirm if they want to play
    def play(self):
        while self._confirm == '':
            self._confirm = input("Do you want to play? Type either 'yes' or 'no' \n ")
            if self._confirm.lower() == "yes":
                # Guess the word
                print("Here is your word to guess")
                print(len(chosen_word) * "_")
            elif self._confirm.lower() == "no":
                print("Goodbye")
            elif self._confirm != "yes" or self._confirm != "no":
                print("Please input yes or no.")

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
                if len(guess_input) > 1:
                    print("Stop cheating")
                elif guess_input != guess_input.isalpha():
                    print("Enter a letter")
                elif guess_input.isnumeric():
                    print("Please do not guess numbers")

                # If we guess the letter correctly
                if guess_input in chosen_word.lower():
                    print("Good job, you guessed a letter correctly")
                    self.guess.append(guess_input)
                    index = self.findoccurrences(chosen_word, guess_input)
                    for i in index:
                        self._underscore[i] = guess_input
                    print(self._underscore)
                    if self._underscore == list(chosen_word):
                        print("Congratulations, you have guessed correctly!")
                        print("The word is:")
                        print(chosen_word.upper())
                        quit()
                else:
                    print("Incorrect, try again \n")
                    print(f"You have {self.tries - 1} tries left")
                    self.tries -= 1

    # Create a method for when the user fails
    def fail(self):
        if self.tries == 0:
            print("You have lost. \n Goodbye.")


try_game = Game()

