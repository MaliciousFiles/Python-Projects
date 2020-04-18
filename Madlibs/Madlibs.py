"""
This program generates passages that are generated in mad-lib format
Author: @MaliciousFiles
Contributors: @mrmaxguns
Copyright (c) 2020 MaliciousFiles All Rights Reserved.
"""

# Imports
from os import path
import random


# Get the template text file
def get_template():
    # Get the template file path
    file = input('Please enter the file you wish to use as a template (type "s" for the sample template): ')

    # Automatic sample
    if file.lower() == 's':
        file = 'my_madlibs/sample.txt'

    # Check if the file path is valid
    if path.exists(file):
        return file
    else:
        raise FileNotFoundError('the file "%s" was not found' % file)


# Get all the words to be replaced from the template
def get_words_from_template(file_path):
    # Open and read the file
    file = open(file_path, 'r')
    file_lines = file.readlines()
    file_lines = ''.join(file_lines)
    file.close()

    # Log the amount of nouns, verbs, and adjectives
    nouns = 0
    verbs = 0
    adjectives = 0

    # Store other replaced word types in this list
    other = []


    # Loop through the file to find all the 'blanks'/things being replaced
    for i in file_lines.split():
        if i == '[noun]':
            nouns += 1
        elif i == '[verb]':
            verbs += 1
        elif i == '[adjective]':
            adjectives += 1
        elif i[0] == '[' and i[-1] == ']':
            other.append(i[1:-1])
        else:
            pass

    # Return a list of all the 'blanks'/things being replaced
    return [nouns, verbs, adjectives, other]


# Get the words from the user
def grab_info(words_list):
    # Get the 'blanks'
    nouns = words_list[0]
    verbs = words_list[1]
    adjectives = words_list[2]
    other = words_list[3]

    # Create lists where the user-chosen words will be stored
    nounslist = []
    verbslist = []
    adjectiveslist = []
    other_words_dict = {}

    # Ask the user for words to replace the 'blanks' and store them in the previously created variables
    if nouns != 0:
        nounslist = []
        for i in range(nouns):
            nounslist.append(input('Give me a noun: '))

    if verbs != 0:
        verbslist = []
        for i in range(verbs):
            verbslist.append(input('Give me a verb: '))

    if adjectives != 0:
        adjectiveslist = []
        for i in range(adjectives):
            adjectiveslist.append(input('Give me an adjective: '))

    if len(other) != 0:
        other_words_dict = {}
        for i in range(len(other)):
            other_words_dict[other[i]] = input('Give me a(n) %s: ' % other[i].replace('-', ' '))

    # Return the lists in a list
    return [nounslist, verbslist, adjectiveslist, other_words_dict]


# Generate the madlib
def return_madlib(final_words_list, file):
    # Get all the word lists
    nouns = final_words_list[0]
    verbs = final_words_list[1]
    adjectives = final_words_list[2]
    other = final_words_list[3]

    # Read the file
    file = open(file, 'r')
    lines = file.readlines()
    lines = ''.join(lines)
    file.close()

    # Create the list with all the words in the madlib
    final_list = []

    # Copy the madlib to the final_list and replace the things in [] with the user-chosen words
    for i in lines.split():
        if i[0] == '[' and i[-1] == ']':
            if i == '[noun]':
                noun = random.choice(nouns)
                final_list.append(noun)
                nouns.remove(noun)
            elif i == '[verb]':
                verb = random.choice(verbs)
                final_list.append(verb)
                verbs.remove(verb)
            elif i =='[adjective]':
                adjective = random.choice(adjectives)
                final_list.append(adjective)
                adjectives.remove(adjective)
            else:
                word = other[i[1:-1]]
                final_list.append(word)
                # other.pop(word)
                other = {key:val for key, val in other.items() if val != word}
        else:
            final_list.append(i)

    # Return the string madlib by joining the final_list
    return ' '.join(final_list)
    

# Connect all of the functions together
def do_the_mad_lib():
    template = get_template()
    info = grab_info(get_words_from_template(template))
    print(return_madlib(info, template))


# Main loop
print('Welcome to madlib!')
while True:
    do_the_mad_lib()

    play_again = input('\nDo you want to play again? (yes/no) ').lower()
    if play_again.startswith('n'):
        print('Thanks for playing!')
        break
