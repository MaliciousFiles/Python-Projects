'''
The game runner.
Author: MaliciousFiles (https://github.com/MaliciousFiles)
Contributor(s): mrmaxguns (https://github.com/mrmaxguns)

Currently supports:
* hangman
* guess the number
'''

# Imports
from hangman import hangman
from guess_the_number import num_game

# The title
title = 'Fun and classic games'

# Draw and "beautify" the title
print('-' * len(title))
print(title)
print('-' * len(title))

# Help menu
help = """

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

"""

# Info menu
info = """

Info
----
Some information about us:
Creator: MaliciousFiles (https://github.com/MaliciousFiles)
Contributors: mrmaxguns (https://github.com/mrmaxguns)

This is open source software. We would love you to contribute.
Just fork the repository (github.com/MaliciousFiles/Python-Projects).

"""

Playing = True

# Main loop
while Playing:
    # Print basic information
    print('\nType "help" to get help, "info" for info, "q" for quit or the name of the game you want to play!\n')

    # Get user input
    command = input('Your wish is my command: ').lower()

    # Run different commands depending on what the user said
    if command.startswith('q'):
        print('\nThanks for playing! See you next time.')
        quit()
    elif command == 'help':
        print(help)
    elif command == 'info':
        print(info)
    elif command.startswith('h'):
        print('Hangman!\n')

        while True:
            hangman()
            again = input('Do you want to play again? y/n ')
            if again.lower().startswith('n'):
                print('\nThanks for playing hangman!')
                break
    elif command.startswith('g'):
        print('Guess the number!')

        while True:
            num_game()
            again = input('Do you want to play again? y/n ')
            if again.lower().startswith('n'):
                print('\nThanks for playing guess the number!')
                break
    else:
        print('Invalid Command')
        print('Please type help for a full list of commands')
