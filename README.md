# HANGMAN

Hangman is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Hangman is a popular word guessing game where the player attempts to build a missing word by guessing one letter at a time. Each incorrect guess brings you closer to being "Hanged".  The game ends when the user runs out of lives or when the player correctly guesses all the letters of the missing word.

More information can be found on the Hangman [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))

![Responsice Mockup](https://github.com/colmhaugh/hangman-game/blob/main/images/am_i_responsive.JPG)

[Here is the live version of my project](https://hangman-cip3.herokuapp.com/)

## How to play

The object of the game is to guess the letters of the hidden word.  The player will have 6 lives.  The user will lose a life for every incorrect guess.

There are 3 categories to choose from:

* Movies

* TV Shows

* Cartoons

The player selects a category and a word or words are randomly picked from that list.

Each letter in the word is represented by a "*".

When the user guesses correctly then the correct letter replaces the "*".

When the player enters an incorrect letter they will lose a life and another piece will be added to the hangman.

To win the game, the player must guess the correct word before all their lives are lost.

## Features

* Welcome Screen

    * Welcomes the user to the game

    ![Welcome Graphic](https://github.com/colmhaugh/hangman-game/blob/main/images/Welcome_Graphic.JPG)

    * Gives brief instructions on how to play

    ![Instructions](https://github.com/colmhaugh/hangman-game/blob/main/images/Instructions.JPG)

    * A graphic of hangman is printed on the screen

    ![Hangman Graphic](https://github.com/colmhaugh/hangman-game/blob/main/images/Choice_with_hangman.JPG)

* Game Menu    

    * Accepts user input, the user has 4 options

        * Movies

        * TV Shows

        * Cartoons

        * Quit
    
    ![Menu Category](https://github.com/colmhaugh/hangman-game/blob/main/images/Menu_Category.JPG)

* Input validation and error-checking

    * Game Menu

        * Player must select a number between 1 and 4 

        * Player will be prompted if they enter a wrong character
    
    * Guessing

        * Player cannot enter the same guess twice

        * Player can only enter 1 letter at a time

        * Player must select a character from the alphabet

* Random Word Generator

    * Takes a random word from the list of the category the player selected

* Length of the word is given and the letters are represented by "*"

* When the player guesses a correct letter the "*" is replaced by that letter

* When the game is completed, the player has the option to play again or quit

## Data Model

* The games starts with a Welcome function which uses time.sleep delay to welcome the player to the game.  Text "Welcome to ..." is printed before a second delay and then the graphic of "HANGMAN" is printed on the screen.  There is another second delay before the basic instructions are given to the user

* A while loop is then used.  The game will stay open until the user quits which breaks the loop

* A menu list is created with 3 game options and a quit option

* The get_random_word function is called to get a random word from the category list the user selected

* A display_hangman function which has the hangman graphics.  This is called in the play_game and changes when the player loses a life for an incorrect guess

* The random word is passed to the play_game function.  

    * Used "re.sub" to have a space instead of a * for a blank space if there were multiple words in the random value

    ![Game with blanks](https://github.com/colmhaugh/hangman-game/blob/main/images/Game_with_blank.JPG)

    * The player can enter their letters here 

        * When a correct letter is guessed, the user gets a prompt to say it is correct and the "*" in the hidden word is replaced with the correct letter

        * When an incorrect guess is entered, the user gets a message, the lives are decreased by 1 and the next graphic of the hangman is printed

    * When the game is completed, the user has an option to play again or to quit

## Technologies

### Languages

* Python3

### Libraries

* Random is used to get a random title from the selected list

* re is imported.  re.sub is used to search and replace so that no "*" is used for a space

* Time is used to give a delay to control the welcome display

## Testing

I have manually tested this project by doing the following:

   * Passed the code through a [PEP8 linter](http://pep8online.com/)

   * Tested main menu section by entering invalid inputs like a number greater than 4 and entering letters and characters

   * Tested the game by entering the same letter twice, entering multiple letters, entering numbers and characters that are not in the alphabet

   * Tested the play again function by entering any key to exit and by entering "y" or "yes" to play again

## Bugs

### Solved Bugs

* There were multiple errors after passing the code through PEP8.  Spaces not multiple of 4 and text length was too long.  Manually fixed all of these

* Solved the issue with multiple words that had spaces.  I didn't want a * where there was a space so used re.sub to solve this issue

### Remaining Bugs

* None

### Validator testing

* PEP8

    * No errors found

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

   * Steps for deployment:

       * Fork or clone this repository

       * Create a new Heroku app

       * Set the buildpacks to Python and NodeJS in that order

       * Link the Heroku app to the repository

       * Click on Deploy

## Credits

* Great advice and guidance from my mentor Precious Ijege

* Great leadership and guidance from Kasia Bogucka

* Code Institute for the deployment terminal

* Code ideas for the Handman game from [AskPython](https://www.askpython.com/python/examples/hangman-game-in-python)

* Stackoverflow for having spaces between multiple words

* Refresh python code from Code Institute lessons and from [w3school](https://www.w3schools.com)