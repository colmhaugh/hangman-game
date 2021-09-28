import random
# Create 3 game options

category = {1: "Movies", 2: "TV Shows", 3: "Cartoons"}

# Each category will have a list or corresponding values
dataset = {"Movies":["THE DARK KNIGHT", "JOKER", "THE GODFATHER", "GLADIATOR", "THE DEPARTED", "ALIEN", "MENENTO", "RESERVOIR DOGS", "FULL METAL JACKET"],\
                 "TV Shows":["BREAKING BAD", "THE GOOD WIFE", "GAME OF THRONES", "THE WIRE", "SUCCESSION", "BILLIONS", "BAND OF BROTHERS", "CHERNOBYL", "TRUE DETECTIVE"],
                 "Cartoons":["DUCKTALES", "ANIMANIACS", "TRANSFORMERS", "THE REAL GHOSTBUSTERS", "THUNDERCATS", "SPONGEBOB SQUAREPANTS", "GRAVITY FALLS", "SMURFS"]
                 }
def get_random_word(option):
    """
    Function to get a random word
    """
    word = random.choice(dataset[option])
    return word.upper()

# Creates a menu with 3 game options and a quit option

for key in category:
    print("For",category[key],  "-> Press", key)
print()
print("Please press", len(category)+1, "to quit") 
print()  

option_selected = int(input("Please chose an option: "))
option_dataset = category[option_selected]
#print(option_dataset)

print(get_random_word(option_dataset))
