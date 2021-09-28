import random
import time
# Create 3 game options

category = {1: "Movies", 2: "TV Shows", 3: "Cartoons"}

# Each category will have a list or corresponding values
dataset = {"Movies":["THE DARK KNIGHT", "JOKER", "THE GODFATHER", "GLADIATOR", "THE DEPARTED", "ALIEN", "MENENTO", "RESERVOIR DOGS", "FULL METAL JACKET"],\
                 "TV Shows":["BREAKING BAD", "THE GOOD WIFE", "GAME OF THRONES", "THE WIRE", "SUCCESSION", "BILLIONS", "BAND OF BROTHERS", "CHERNOBYL", "TRUE DETECTIVE"],
                 "Cartoons":["DUCKTALES", "ANIMANIACS", "TRANSFORMERS", "THE REAL GHOSTBUSTERS", "THUNDERCATS", "SPONGEBOB SQUAREPANTS", "GRAVITY FALLS", "SMURFS"]
                 }


# Creates a menu with 3 game options and a quit option
def game_menu():
    """
    Displays the game menu and asks user to select an option of what game to play
    """
    print("Welcome to...")
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
    #print(insructions)

    for key in category:
        print("For",category[key],  "-> Press", key)
    print()
    print("Please press", len(category)+1, "to quit") 
    print()  

    option_selected = int(input("Please choose an option: "))
    option_dataset = category[option_selected]
#print(option_dataset)
    return get_random_word(option_dataset)
    #print(get_random_word(option_dataset))

def get_random_word(option):
    """
    Function to get a random word
    """
    word = random.choice(dataset[option])
    return word.upper()

def hide_word():
    """
    Function prints row of stars in place of letters.
    """
    myword = game_menu()

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

def main():
    
    #game_menu()
    i = 6
    while i > 1:              
        print(display_hangman(i))
        i -= 1

main()


