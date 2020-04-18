from random import choice

def hangman():
    wordfile = open('words/words.txt', 'r')
    lines = wordfile.readlines()
    wordfile.close()

    wordlist = [i.rstrip() for i in lines]

    word = choice(wordlist)
    guess_instances={}
    wordguess=''
    guesspool=[]

    for x in range(len(word)):
        wordguess+='_ '

    hung_parts=0
    new_part=''
    hungman='''
   ______
   |    |
   |    |
   |
   |
   |
   |
   |
'''
    while hung_parts < 6:
        print(hungman)
        print(wordguess)

        guess = input('Guess a letter\n').lower()

        if guess in guesspool:
            print('You have already guessed %s! Guess again.'%guess)
        elif len(guess)>1 or len(guess)<1 or guess.isalpha() == False:
            print('Not a letter! Guess again.')
        else:
            if guess in word:
                for let in range(len(word)):
                    if word[let] == guess:
                        guess_instances[let] = guess

                guess_times = 0

                for key in guess_instances:
                    h = guess_instances.get(key)
                    if h == guess:
                        guess_times += 1

                if guess_times == 1:
                    print('There was 1 %s'%guess)
                elif guess_times>1:
                       print('There were '+str(guess_times)+' '+guess+'\'s')

                x = 0
                wordguessn = ''
                guess_instancesn = {}

                for n in range(0,9):
                    j = True
                    h = guess_instances.get(n)
                    if h == None:
                        j = False
                    if j:
                        guess_instancesn[n] = guess_instances[n]

                guess_instances = guess_instancesn

                for key in guess_instances:
                    while x < key:
                        wordguessn += '_ '
                        x += 1
                    wordguessn += '%s '%guess_instances[key]
                    x+=1

                while len(wordguessn)<len(wordguess):
                    wordguessn+='_ '

                wordguess=wordguessn

            else:
                hung_parts+=1

                if hung_parts==1:
                    new_part='a head'
                elif hung_parts==2:
                    new_part='a body'
                elif hung_parts==3:
                    new_part='an arm'
                elif hung_parts==4:
                    new_part='an arm'
                elif hung_parts==5:
                    new_part='a leg'
                elif hung_parts==6:
                    new_part='a leg'

                print('You got %s!'%new_part)

                if hung_parts==1:
                    hungman='\n\n   ______\n   |    |\n   |    |\n   |    o\n   |    \n   |    \n   |\n'
                elif hung_parts==2:
                    hungman='\n\n   ______\n   |    |\n   |    |\n   |    o\n   |    | \n   |    \n   |\n'
                elif hung_parts==3:
                    hungman='\n\n   ______\n   |    |\n   |    |\n   |    o\n   |    |\\ \n   |    \n   |\n'

                elif hung_parts==4:
                    hungman='\n\n   ______\n   |    |\n   |    |\n   |    o\n   |   /|\\ \n   |     \n   |\n'
                elif hung_parts==5:
                    hungman='\n\n   ______\n   |    |\n   |    |\n   |    o\n   |   /|\\ \n   |   / \n   |\n'
                elif hung_parts==6:
                    print('\n\n   ______\n   |    |\n   |    |\n   |    o\n   |   /|\\ \n   |   / \\ \n   |\n\nYou lose! The word was %s.\n'%word)
        if '_' not in wordguess:
            print('%s\n\nYou win!'%hangman)

        guesspool+=guess


if __name__ == "__main__":
    hangman()
