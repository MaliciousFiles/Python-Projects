maxnumber=0
import time
trytally=0
def numbergame(difficulty):
        global maxnumber
        global trytally
        if difficulty=="easy":
            maxnumber=30
            trytally=6
        if difficulty=="medium":
            maxnumber=40
            trytally=4
        if difficulty=="hard":
            maxnumber=50
            trytally=4
        if difficulty=="crazy":
            maxnumber=100
            trytally=7
while True:
        exec(input('Type "numbergame()" and in the parentheses type either "easy", "medium", "hard",\nor "crazy" depending on how hard you want it to be.\n'))
        tries=int(round(maxnumber/trytally,0))
        from random import randint
        pickednumber=randint(1,maxnumber)
        triesexceeded=0
        try:
            inputa=int(input("I am thinking of a number between 1-%s. You have %s tries left.\nWhat number am I thinking of?\n"%(maxnumber,tries)))
        except:
            print("Not a number. You lose")
            quit()
        if  inputa==pickednumber:
            print("Good Job!\nYou won in %s tries"%(int(round(maxnumber/trytally,0))-tries+1))
            if input("Do you want to play again?\n")[0]=="y":
                tries=int(round(maxnumber/trytally,0))
                print("Have Fun!\n")
                triesexceeded=1
            else:
                print("Thanks for playing!")
                time.sleep(2)
                quit()
        else:
            if tries==1:
                print("You lose!\nYou took too many tries.")
                if input("Do you want to play again?\n")[0]=="y":
                    tries=int(round(maxnumber/trytally,0))
                    print("Have Fun!\n")
                    triesexceeded=1
                else:
                    print("Thanks for playing!")
                    time.sleep(2)
                    quit()
            if inputa<pickednumber and triesexceeded==0:
                print("Too low.\nTry Again!")
                tries=tries-1
            if inputa>pickednumber and triesexceeded==0:
                print("Too high.\nTry Again!")
                tries=tries-1
                
            


