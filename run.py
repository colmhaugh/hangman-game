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
    Function prints row of stars in place of letters.
    """
    myword = gameword

    for i in myword:         
        print("*", end = " ") 
        
    # Calculating length of word 
    l = len(myword) 
    print("Word has %d letters" %l)

def display_hangman(lives):
    """
    index stage that corresponts with the number of lives player have
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
   hidden_word = hide_word(word)
   guessed = False
   guessed_letters = []
   guessed_words = []
   lives = 6
   print(display_hangman(lives))
   while not guessed and lives > 0:
      guess = input("guess a letter or word: ").upper()
      if len(guess) == 1 and guess.isalpha():
         if guess in guessed_letters:
            print("you already tried", guess, "!")
         elif guess not in word:
            print(guess, "isn't in the word :(")
            lives -= 1
            guessed_letters.append(guess)
         else:
            print("Nice one,", guess, "is in the word!")
            guessed_letters.append(guess)
            word_as_list = list(hidden_word)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
               word_as_list[index] = guess
            hidden_word = "".join(word_as_list)
            if "_" not in hidden_word:
               guessed = True
      elif len(guess) == len(word) and guess.isalpha():
         if guess in guessed_words:
            print("You already tried ", guess, "!")
         elif guess != word:
            print(guess, " ist nicht das Wort :(")
            lives -= 1
            guessed_words.append(guess)
         else:
            guessed = True
            hidden_word = word
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

        for key in category:
            print("For",category[key],  "-> Press", key)
        print()
        print("Please press", len(category)+1, "to quit") 
        print()

        # Handling the player category choice
        try:
            option_selected = int(input("Enter Your Choice = \n"))
        except ValueError:
            clear()
            print("Invalid Choice!!! Try Again")
            continue

        # Sanity checks for input
        if option_selected > len(category)+1:
            clear()
            print(f"{option_selected} is not an option.  Please select a number between 1 and 4")
            continue

        # The EXIT choice
        elif option_selected == len(category)+1:
            print()
            print("Thank You For Playing!")
            break
      
        game_word = get_random_word(option_selected)
        play_game(game_word)
        #hide_word(game_word)
        break
        
        #hide_word()

      
    
      
    
    
            
        


