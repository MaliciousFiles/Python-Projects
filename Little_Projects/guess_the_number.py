from random import randint, choice

def num_game(range=50, num_of_tries=5):

    num = randint(1, range)
    tries = num_of_tries

    while tries > 0:
        print('')

        guess = input('Guess a number from 1 to %s. You have %s trie(s) left.\n' % (range, tries))

        try:
            guess = int(guess)
        except ValueError:
            print('%s is not an integer! Try again' % guess)
            continue

        if guess < range and guess > 0:

            if guess == num:
                print('You WIN!!!')
                break
            elif guess > num and tries > 1:
                print('%s is too high. Try again.' % guess)
                tries-=1
            elif guess<num and tries > 1:
                print('%s is too low. Try again.' % guess)
                tries-=1
            elif tries == 1:
                tries -= 1

        else:
            print('%s is not in range! Try again.' % guess)

    if tries == 0:
        print('Oh no, you ran out of tries. I WIN!!!!!!!!!!!')

if __name__ == "__main__":
    num_game()
