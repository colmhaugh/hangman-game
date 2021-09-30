import random
import os
import time


# Create 3 game options

category = {1: "Movies", 2: "TV Shows", 3: "Cartoons"}

# Each category will have a list or corresponding values
dataset = {"Movies":["THE DARK KNIGHT", "JOKER", "THE GODFATHER", "GLADIATOR", "THE DEPARTED", "ALIEN", "MENENTO", "RESERVOIR DOGS", "FULL METAL JACKET"],\
                 "TV Shows":["BREAKING BAD", "THE GOOD WIFE", "GAME OF THRONES", "THE WIRE", "SUCCESSION", "BILLIONS", "BAND OF BROTHERS", "CHERNOBYL", "TRUE DETECTIVE"],
                 "Cartoons":["DUCKTALES", "ANIMANIACS", "TRANSFORMERS", "THE REAL GHOSTBUSTERS", "THUNDERCATS", "SPONGEBOB SQUAREPANTS", "GRAVITY FALLS", "SMURFS"]
                 }

# Funtion to clear te terminal
def clear():
    os.system("clear")

def get_random_word(option):
    """
    Function to get a random word
    from the list of the category
    that the user selected
    """
    option_selected = int(option)
    option_dataset = category[option_selected]
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
        print("*", end = " ") 
    print()
    # Calculating length of word 
    l = len(myword) 
    print("Word has %d letters" %l)

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

def play_game(word):
   """
   Will use the random word that is passed and use
   the hide_word function to show * in stead of letters.   
   """
   
   # Takes the word that was passed into it and prints out 
   # * in place of the letters 
   #hidden_word = hide_word(word)
   hidden_word = "*" * len(word)
   guessed = False
   # List of letters guessed. Will be appended with each guess
   guessed_letters = []   
   # User starts with 6 lives, will decrease by 1 for every incorrect 
   # guess and will be passed to the display_hangman
   lives = 6
   # Prints the image  of hangman
   print(display_hangman(lives))
   print(hidden_word)
   print("\n")

   while not guessed and lives > 0:
      guess = input("Please guess a letter: ").upper()
      # Checks if the user entered 1 word and it is s letter
      if len(guess) == 1 and guess.isalpha():
         # Checks if the letter is in the guessed_letters list so it has already been guessed
         if guess in guessed_letters:
            # If the letter was already geussed the user will be told
            print("you already tried", guess, "!")
         # Checks if the guessed letter is not in the hidden word   
         elif guess not in word:
            print(guess, "isn't in the word :(")
            # User loses a life which will be passed to hangman image
            lives -= 1
            # Add letter to the guessed_letters list
            guessed_letters.append(guess)
         else:
            print("Nice one,", guess, "is in the word!")
            # Add letter to the guessed_letters list
            guessed_letters.append(guess)
            # 
            word_as_list = list(hidden_word)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
               word_as_list[index] = guess
            hidden_word = "".join(word_as_list)
            if "*" not in hidden_word:
               guessed = True      
      else:
         print("invalid input")
      print(display_hangman(lives))
      print(hidden_word)
      print("\n")
   if guessed:
      print("Good Job, you guessed the word!")
   else:
      print("I'm sorry, but you ran out of tries. The word was " + word + ". Maybe next time!")



if __name__ == "__main__":
    clear()
    
    # The GAME LOOP
    while True:

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

        # Create a list of options from the categories
        for key in category:
            print("For",category[key],  "-> Press", key)
        print()
        # Add an option for quitting which will be 1 greater then the ammount of categories on the list
        print("Please press", len(category)+1, "to quit") 
        print()

        # Handling the player category choice
        try:
            option_selected = int(input("Enter Your Choice = \n"))
        except ValueError:
            clear()
            print("Invalid Choice!!! Try Again")
            continue

        # Checks if the user selected a number that was not on the list
        if option_selected > len(category)+1:
            clear()
            print(f"{option_selected} is not an option.  Please select a number between 1 and 4")
            continue

        # The EXIT choice number is the number of choices plus 1
        elif option_selected == len(category)+1:
            print()
            print("Thank You For Playing!")
            break
      
        game_word = get_random_word(option_selected)
        play_game(game_word)
        #hide_word(game_word)
        break
        
      
    
      
    
    
            
        


