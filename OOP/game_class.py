import brain_class as bc
# Import word from brain class
winning_word = bc.winning_word.get_word()

class Game:

    # Initialise function to welcome the user
    def __init__(self):
        self.tries = 7
        print("Welcome to Hangman!")

    # Method to ask the user to confirm if they want to play
    def play(self):
        confirm = input("Do you want to play? Type either 'yes' or 'no' ")

        if confirm.lower() == "yes":
            # Guess the word
            print("Here is your word to guess")
            print(winning_word)
        else:
            print("Goodbye")

    # Main body of the game
    # Function to find occurrences letters

    def findoccurrences(self, s, ch):
        return [i for i, letter in enumerate(s) if letter == ch]

    # Hangman game
    def hangman(self):
        while self.tries > 0:

            guess = input("Please guess a letter. \n")
            if 0 < len(guess) > 1:
                print("Stop cheating")
            elif guess.isnumeric():
                print("Please do not guess numbers")
            elif guess.lower() in winning_word:
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
