import random
print("This is called the Rhino Game.\nI will give you an amount of rhinos and you tell me how many there are.\nThis probalbly dosn't make sense so let me show you.")
while True:
    if input("\nPress ENTER to start.\n")=="Poof Rules":
        print("\n\nThe Rule:\nThe number of syllabels in the question.\n\n")
    whattoprint=["How many rhinos are there?","How many?","How many rhinos?","How many rhinos are there on you?"]
    random.shuffle(whattoprint)
    amt=random.randint(1,100)
    place=["in your nose","in your hair","in your eye sockets"]
    random.shuffle(place)
    amt=random.randint(1,100)
    print("There are %s rhinos %s"%(amt,place[0]))
    random.shuffle(whattoprint)
    random.shuffle(place)
    amt=random.randint(1,100)
    print("There are %s rhinos %s"%(amt,place[0]))
    random.shuffle(place)
    amt=random.randint(1,100)
    print("There are %s rhinos %s"%(amt,place[0]))
    random.shuffle(whattoprint)
    random.shuffle(place)
    amt=random.randint(1,100)
    random.shuffle(whattoprint)
    inputa=input("%s\n"%whattoprint[0])
    if whattoprint[0]=="How many rhinos are there?" and inputa=="7":
        if input("You win! Do you want to play again?\n")[0].lower()=="y":
            pass
        else:
            quit()
    elif whattoprint[0]=="How many?" and inputa=="3":
            if input("You win! Do you want to play again?\n")[0].lower()=="y":
                pass
            else:
                quit()
    elif whattoprint[0]=="How many rhinos?" and inputa=="5":
        if input("You win! Do you want to play again?\n")[0].lower()=="y":
            pass
        else:
            quit()
    elif whattoprint[0]=="How many rhinos are there on you?" and inputa=="9":
            if input("You win! Do you want to play again?\n")[0].lower()=="y":
                pass
            else:
                quit()
    else:
        if whattoprint[0]=="How many rhinos are there?":
            print("Wrong! There are 7 rhinos.")
        elif whattoprint[0]=="How many?":
             print("Wrong! There are 3 rhinos.")
        elif whattoprint[0]=="How many rhinos?":
            print("Wrong! There are 5 rhinos.")
        elif whattoprint[0]=="How many rhinos are there on you?":
            print("Wrong! There are 9 rhinos.")
