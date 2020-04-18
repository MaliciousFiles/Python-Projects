"""
This program generates passages that are generated in mad-lib format
Author: @MaliciousFiles
Contributors: @mrmaxguns
Copyright (c) 2020 MaliciousFiles All Rights Reserved.
"""

from os import path
import random

def get_template():
    file = input('Please enter the file you wish to use as a template (type "s" for the sample template): ')
    if file.lower() == 's':
        file = 'my_madlibs/sample.txt'

    if path.exists(file):
        return file
    else:
        raise FileNotFoundError('the file "%s" was not found' % file)

def get_words_from_template(file_path):
    file = open(file_path, 'r')
    file_lines = file.readlines()
    file_lines = ''.join(file_lines)
    file.close()

    nouns = 0
    verbs = 0
    adjectives = 0
    other = []


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

    return [nouns, verbs, adjectives, other]

def grab_info(words_list):
    nouns = words_list[0]
    verbs = words_list[1]
    adjectives = words_list[2]
    other = words_list[3]

    nounslist = []
    verbslist = []
    adjectiveslist = []
    other_words_dict = {}

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

    return [nounslist, verbslist, adjectiveslist, other_words_dict]

def return_madlib(final_words_list, file):
    nouns = final_words_list[0]
    verbs = final_words_list[1]
    adjectives = final_words_list[2]
    other = final_words_list[3]

    file = open(file, 'r')
    lines = file.readlines()
    lines = ''.join(lines)
    file.close()

    final_list = []
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

    return ' '.join(final_list)

def do_the_mad_lib():
    template = get_template()
    info = grab_info(get_words_from_template(template))
    print(return_madlib(info, template))


print('Welcome to madlib!')
while True:
    do_the_mad_lib()

    play_again = input('\nDo you want to play again? (yes/no) ').lower()
    if play_again.startswith('n'):
        print('Thanks for playing!')
        break
