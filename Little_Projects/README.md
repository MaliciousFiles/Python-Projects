# Little Projects (Aka. Games)
Here are some fun little games that you can play. Don't even worry about all of the different python files. Just run `run.py` and choose a game to play! Games supported include hangman and guess the number. Info on all games can also be found in the docs folder.

## Table of contents
* [Current file structure](#Current-file-structure)
* [Accessing the projects](#Accessing-the-projects)
* [Supported games](#Supported-games)


## Current file structure
```
/Little_Projects
+-- __pycache__               <-- Developers, ignore this directory
|   |-- guess_the_number.cpython-36.pyc
|   |-- hangman.cpython-36.pyc
+-- docs
|   |-- hangman.md
|   |-- guess_the_number.md
+-- words
|   |-- words.txt
+-- words
+-- guess_the_number.py
+-- hangman.py
+-- README.md
+-- run.py
+-- guess_the_number.pyc   <-- Developers, ignore this file
+-- hangman.pyc  <-- Developers, ignore this file
```

The `__pycache__` is used by python and can be safely ignored. The `docs` directory contains a documentation on the games. The `words` directory contains files needed for `hangman.py`. There is also `guess_the_number.py`, `hangman.py` and `run.py`. The only important python file for users is `run.py` where you can access all of the games.

## Accessing the projects
Here are the steps, as a user to play these games.

1. Run the python program `run.py`. You can do this with python shell, or the command prompt. Here we will show you the command prompt code to run the program (make sure you are in the `Little_Projects` directory)
  ```
  $ python run.py
  ```
2. You will then get a prompt like this:
  ```
  ---------------------
  Fun and classic games
  ---------------------

  Type "help" to get help, "info" for info, "q" for quit or the name of the game you want to play!

  Your wish is my command:
  ```
  As you can see, we currently do not support a GUI, so you can access the games by typing commands.

2. Type help to get a list of all the commands:

  ```
  Your wish is my command: help

  Help!
  -----
  Welcome to the help section. Here are basic instructions. Be sure to look at "README.md" and the "docs" folder for more info.

  Basic operation:
  * "q": quit
  * "help": open this help menu thing
  * "info": for info on the creators and how you can contribute

  Games:
  * "hangman" to play the classic hangman game
  * "gtn" or "guess the number" to play guess the number
  ```
3. Type all commands after the `Your wish is my command: `
4. To quit, type `q`
5. To play a game, type the game command (see below).

## Supported games
* Hangman: **type: "hangman"** to play. Hangman is the classic game where the computer thinks of a word and then the player guesses letters from it. See `hangman.md` in the `docs` folder.
* Guess the number: **type: "gtn" or "guess the number"** to play. Guess the number is a game where the computer generates a random number and you guess it. You have limited chances and all the computer tells you if the number is too high or too low. See `guess_the_number.md` in the `docs` folder.
