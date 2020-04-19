'''
The classic guess the number game
Author: MaliciousFiles (https://github.com/MaliciousFiles)
Contributor(s): mrmaxguns (https://github.com/mrmaxguns)
'''

# Imports
from random import randint

# Main function
def num_game(range=50, num_of_tries=5):

    # Choose the random number
    num = randint(1, range)

    # Set the number of tries to the specified parameter
    tries = num_of_tries

    # The main game loop runs until there are no tries left
    while tries > 0:
        # Get the user's guess
        guess = input('\nGuess a number from 1 to %s. You have %s try/tries left.\n' % (range, tries))

        # Try to turn the guess into an integer
        try:
            guess = int(guess)
        except ValueError:
            # If a ValueError is raised, alert the user to enter an integer
            print('%s is not an integer! Try again' % guess)
            continue

        # Check if the guess is in the guessing range
        if guess < range and guess > 0:

            # Excecute if the guess is the random number
            if guess == num:
                print('You WIN!!!')
                break
            # Excecute if the guess is too high
            elif guess > num:
                print('%s is too high. Try again.' % guess)
                tries-=1
            # Excecute if the guess is too low
            elif guess < num :
                print('%s is too low. Try again.' % guess)
                tries-=1

        # Excecute if the number is not in the guessing range
        else:
            print('%s is not in range! Try again.' % guess)

    # Tell the player they lost if tries have run out
    if tries == 0:
        print('Oh no, you ran out of tries. I WIN!!!!!!!!!!!')

# Run the function if this module is run
if __name__ == "__main__":
    num_game()
