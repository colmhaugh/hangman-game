import random
import os
import time
import re

# Create 3 game options

category = {1: "Movies", 2: "TV Shows", 3: "Cartoons"}

# Each category will have a list or corresponding values
dataset = ({"Movies": [
   "THE DARK KNIGHT", "JOKER", "THE GODFATHER",
   "GLADIATOR", "THE DEPARTED", "ALIEN", "MENENTO",
   "RESERVOIR DOGS", "FULL METAL JACKET"
   ], "TV Shows": [
      "BREAKING BAD", "THE GOOD WIFE",
      "GAME OF THRONES", "THE WIRE", "SUCCESSION",
      "BILLIONS", "BAND OF BROTHERS", "CHERNOBYL",
      "TRUE DETECTIVE"
      ], "Cartoons": [
         "DUCKTALES", "ANIMANIACS", "TRANSFORMERS",
         "THE REAL GHOSTBUSTERS", "THUNDERCATS", "SPONGEBOB SQUAREPANTS",
         "GRAVITY FALLS", "SMURFS"]
          })


# Funtion to clear the terminal
def clear():
    os.system("clear")


def welcome():
    # Printing the game menu
    print(" Welcome To The Classic Game Of ...")
    # Add delay
    time.sleep(1)
    print('''
               _
               | |
               | |__   __ _ _ __    __ _ _ __ ___    __ _ _ __
               | '_ \ / _` | '_ \ / _'  | '_ ` _ \ /  _` | '_  \.
               | | | | (_| | | | | ( |  | | | | | |  ( | | | | |
               |_| |_|\__,_|_| |_|\__,  |_| |_| |_|\__,_ |_| |_|
                                    __/ |
                                    |__ /                        ''')
    time.sleep(1)


def get_random_word(option):
    """
    Function to get a random word
    from the list of the category
    that the user selected
    """
    option_selected = int(option)
    option_dataset = category[option_selected]
    print(f"You have chosen {option_dataset}")
    word = random.choice(dataset[option_dataset])
    return word.upper()


def hide_word(gameword):
    """
    Function prints row of stars in place of
    letters and  tells the user how many letters
    the word has
    """
    myword = gameword
    print()

    for i in myword:
        if i != " ":
            print("*", end=" ")
    print()
    # Calculating length of random random word
    lench = len(myword)
    print("Word has %d letters" % lench)


def display_hangman(lives):
    """
    Index stage that corresponts with the
    number of lives player have.  User will
    start off with 6 lives and lose a life for
    every incorrect guess until they run our of
    lives.
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \.
                __| |______
                           |_
                _____________|_________
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                __| |______
                           |_
                _____________|_________
                   """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                __| |______
                           |_
                _____________|_________
                   """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                __| |______
                           |_
                _____________|_________
                   """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                __| |______
                           |_
                _____________|_________
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                __| |______
                           |_
                _____________|_________
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                __| |______
                           |_
                _____________|_________
                """
    ]
    return stages[lives]


def play_again():
    print("Press Y if you want to play again")
    print("Press any other letter to finish")
    return input().lower().startswith('y')


def play_game(word):
    """
    Will use the random word that is passed and use
    the hide_word function to show * in stead of letters.
    """
    # Takes the word that was passed into it and prints out
    # * in place of the letters
    # Used re.sub so that it doesnt include spaces
    hidden_word = re.sub(r'\S', '*', word)
    guessed = False
    # List of letters guessed. Will be appended with each guess
    guessed_letters = []
    # User starts with 6 lives, will decrease by 1 for every incorrect
    # guess and will be passed to the display_hangman
    lives = 6
    # Prints the image  of hangman
    print(display_hangman(lives))
    # Prints the * and spaces for the hidden word
    print(hidden_word)

    print("\n")
    # While the user hasn't guessed the word
    # and they still have lives play the game
    while not guessed and lives > 0:
        guess = input("Please guess a letter: ").upper()
        # Checks if the user entered 1 letter and
        # it is a letter in the alphabet
        if len(guess) == 1 and guess.isalpha():
            # Checks if the letter is in the guessed_letters
            # list so it has already been guessed
            if guess in guessed_letters:
                # If the letter was already geussed the user will be told
                print(f"You have alrady guessed {guess}")
                print("Please try a differnt letter")
                # Checks if the guessed letter is not in the hidden word
            elif guess not in word:
                print(f"{guess} isn't in the word :(")
            # User loses a life which will be passed to hangman image
                lives -= 1
                # Add letter to the guessed_letters list
                guessed_letters.append(guess)
            else:
                print(f"Good guess, {guess}, is in the word!")
                # Add letter to the guessed_letters list
                guessed_letters.append(guess)
                # Makes a list of the hidden_word,
                # if the word is in the list then
                # the letter guessed will replace the *
                word_as_list = list(hidden_word)
                indices = [
                   i for i, letter in enumerate(word) if letter == guess
                   ]
                for index in indices:
                    word_as_list[index] = guess
                    hidden_word = "".join(word_as_list)
                if "*" not in hidden_word:
                    guessed = True
        else:
            print("invalid input")
        # Display the current image of hangman
        print(display_hangman(lives))
        print()
        # Display the ammount of lives left
        print(f"You have {lives} lives remaining")
        print(hidden_word)
        print("\n")
    if guessed:
        print("Congratlations, you have guessed the correct word")
        print()
    else:
        print("Hard luck.  You have ran out of lives.")
        print(f"The word was {word}.")
        print()


if __name__ == "__main__":
    clear()
    welcome()
    # The GAME LOOP
    while True:
        print("-------------------------------------------------")
        print("----------PLEASE CHOOSE A CATEGORY---------------")
        print("-------------------------------------------------")
        # Create a list of options from the categories
        for key in category:
            print("For", category[key],  "-> Press", key)
        print()
        # Add an option for quitting which will be 1
        # greater then the ammount of categories on the list
        print("Please press", len(category)+1, "to quit")
        print()

        # Handling the player category choice
        try:
            option_selected = int(input("Enter Your Choice = \n"))
        except ValueError:
            clear()
            print("Invalid Choice! Try Again \n")
            continue

        # Checks if the user selected a number that was not on the list
        if option_selected > len(category)+1:
            clear()
            print(f"{option_selected} is not an option.")
            print(f"Please select a number between 1 and {len(category)+1} \n")
            continue

        # The EXIT choice number is the number of choices plus 1
        elif option_selected == len(category)+1:
            print()
            print("Thank You For Playing.  See you again soon.")
            break

        print()
        game_word = get_random_word(option_selected)
        play_game(game_word)
        # When  the game is complete it calls the play again function
        # If the user presses Y they play again.
        # If the user presses any other key loop will break
        # The game will be over
        if play_again():
            print("Play again")
        else:
            print("Thank You For Playing.  See you again soon.")
            break
