from random import randint,choice
def num_game():
    num=randint(1,50)
    tries=5
    while tries>0:
        guess=input('Guess a number from 1 to 50. You have %s tries left.\n'%tries)
        if ('.' in guess) or guess.isdigit() or (len(guess)>0 and guess[0]=='-' and guess[1:].isdigit()):
            guess = int(guess)
            gues=guess
            guess=round(guess)
            if guess>50 or guess<1:
                print('%s is not in range! Try again.'%guess)
            elif gues!=guess:
                print('Your guess has been rounded.') 
            else:
                if guess==num:
                    if 'y' in input('You win! Do you want to play again?(y/n)\n'):
                        num_game()
                    else:
                        pick_game()
                elif guess>num and tries > 1:
                    print('%s is too high. Try again.'%guess)
                    tries-=1
                elif guess<num and tries > 1:
                    print('%s is too low. Try again.'%guess)
                    tries-=1
                elif tries == 1:
                    tries -= 1
        else:
            print('%s is not a number! Try again.'%guess)
    if 'y' in input('Wrong! You are out of tries. Do you want to play again?(y/n)\n'):
        num_game()
    else:
        pick_game()
def hangman():
    wordlist=['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac']
    word=choice(wordlist)
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
    while hung_parts<6:
        print(hungman)
        print(wordguess)
        guess=input('Guess a letter\n').lower()
        if guess in guesspool:
            print('You have already guessed %s! Guess again.'%guess)
        elif len(guess)>1 or len(guess)<1 or guess.isalpha()==False:
            print('Not a letter! Guess again.')
        else:
            if guess in word:
                for let in range(len(word)):
                    if word[let]==guess:
                        guess_instances[let]=guess
                guess_times=0
                for key in guess_instances:
                    h=guess_instances.get(key)
                    if h==guess:
                        guess_times+=1
                if guess_times==1:
                    print('There was 1 %s'%guess)
                elif guess_times>1:
                       print('There were '+str(guess_times)+' '+guess+'\'s')
                x=0
                wordguessn=''
                guess_instancesn={}
                for n in range(0,9):
                    j=True
                    h=guess_instances.get(n)
                    if h==None:
                        j=False
                    if j:
                        guess_instancesn[n]=guess_instances[n]
                guess_instances=guess_instancesn
                for key in guess_instances:
                    while x<key:
                        wordguessn+='_ '
                        x+=1
                    wordguessn+='%s '%guess_instances[key]
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
                    if 'y' in input('\n\n   ______\n   |    |\n   |    |\n   |    o\n   |   /|\\ \n   |   / \\ \n   |\n\nYou lose! The word was %s. Would you like to play again?(y/n)\n'%word):
                        hangman()
                    else:
                        pick_game()
        if '_' not in wordguess:
            if 'y' in input('%s\n\nYou win! Would you like to play again?(y/n)\n'%hangman):
                hangman()
            else:
                pick_game()

        guesspool+=guess
    
                            #add more definitions as you add more games
def pick_game():
    game=input('Which game would you like to play? The choices are:\n-Guess the Number(\'num game\' for short)\n-Hangman\n-Go Fish\n').lower() #add more choices as you add more games
    if game=='guess the number' or game=='num game':
        num_game()
    elif game=='hangman':
        hangman()
    elif game == 'go fish':
        go_fish()
                            #add elifs as you add more games
    else:
        print('Not an option! Please pick again!\n')
        pick_game()
pick_game()
