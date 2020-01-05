import random
import time
def log_on():
    global activeuser
    data=open("game.txt","a+")
    logged_on = False
    while not logged_on:
        exist=input("Login or Signup?\n")
        if exist.lower()=="login":
            username=input("Username:\n")
            found = False
            data.seek(0)
            for line in data.readlines():
                line = eval(line)
                if line["user"]==username:
                    found = True
                    password=input("Password:\n")
                    if line["pass"]==password:
                        activeuser=line
                        logged_on = True
                    else:
                        print("Wrong password!")
            if not found:
                print("User not found. Please try again or sign up.")
        elif exist.lower()=="signup":
            username=input("Create username:\n")
            found = False
            data.seek(0)
            for line in data.readlines():
                line = eval(line)
                if line["user"]==username:
                    found = True
            if found:
                print("Username already exists. Please try again or log in as an existing user.")
            else:
                setup_new(username)
                data.seek(0)
                activeuser=eval(data.readlines()[-1])
                logged_on = True
        else:
            print("Not 'Login' or 'Signup'")
    data.close()
    if logged_on:
        print("    ---------\n\
     Warning\n\
    ---------\n\n\
If you don't save and log out you will lose your data!\n\n")
def setup_new(username):
    data=open("game.txt","a")
    global activeuser
    activeuser = {}
    activeuser["user"]=username
    activeuser["pass"]=input("Create password:\n")
    activeuser["daily_chest"]=0
    activeuser["creatures"]={"Rocky":creature_database["Rocky"]}
    activeuser["creatures"]["Rocky"]["Xp"]=0
    activeuser["creatures"]["Rocky"]["Xp_needed"]=50
    activeuser["creatures"]["Rocky"]["level"]=1
    add_creature("Flamdring")
    data.write(str(activeuser)+"\n")
    data.flush()

def update_data():
    global activeuser
    data = open("game.txt")
    for line in data.readlines():
        line = eval(line)
        if line["user"] == activeuser["user"]:
            replaceuser = line
    data.seek(0)
    new_text = data.read().replace(str(replaceuser),str(activeuser))
    data.close()
    update = open("game.txt","w")
    
    update.write(new_text)
    update.close()

def intro():
    while True:
        rules=input("Would you like to see the rules?\n")
        if rules[0].lower()=="y":
            print("You have different creature cards.\n\
    You can fight your cards against other peoples' cards.\n\
    If you win, your creature gains XP and you get gold coins.\n\
    When a creature gains enough XP it can level up.\n\
    It costs gold coins to level up your creatures.\n\
    When a creature levels up its stats improve.\n\
    Sometimes you can find a wild creature, which you can collect by fighting one of your creatures cards against it.\
    \n-------\
    \nWarning\
    \n-------\
    \nIf you do not save and log out, all your data since you logged on will be lost!\n")
            break
        elif rules[0].lower()=="n":
            break
        else:
            print("Not an option!")
def game():
    global activeuser
    if random.randint(1,1000)==1000:
        attacking_creature=input("A wild %s apeared! What do you want to attack it with?\n"%random.choice(creature_database_attributes))
        anti_creature=creature_database_attributes[0]
    else:
        while True:
            if time.time()-activeuser["daily_chest"]>=86400:
                daily=True
            else:
                daily=False
            if daily==True:
                doing=input("\nDo you,\n>>>Attack\n>>>Level up your creature cards(Level up)\n>>>Look at your creatures(look at creatures)\n>>>Open daily chest(daily)\n>>>Save and log out(log out)\n")
            else:
                doing=input("\nDo you,\n>>>Attack\n>>>Level up your creature cards(Level up)\n>>>Look at your creatures(look at creatures)\n>>>Save and log out(log out)\n")
            if doing.lower()=="attack":
                attack()
            elif doing.lower()=="level up":
                level_up()
            elif daily==True and doing.lower()=="daily":
                daily_chest()
            elif doing.lower()=="look at creatures":
                display_creatures()
            elif doing.lower()=="log out":
                update_data()
                play()
            else:
                print("Not an option!")


def display_creatures():
    for creature in activeuser["creatures"]:
        print("\b%s:\n    Defense: %s\n    Health: %s\n    Attacks:"%(creature,activeuser["creatures"][creature]["defense"],activeuser["creatures"][creature]["health"]))
        for attack in activeuser["creatures"][creature]["attacks"]:
            print("        %s: Damage: %s"%(attack,activeuser["creatures"][creature]["attacks"][attack]))
        print("\n    Xp: %s\n    Xp Needed: %s\n    Level: %s\n"%(activeuser["creatures"][creature]["Xp"],activeuser["creatures"][creature]["Xp_needed"],activeuser["creatures"][creature]["level"]))
def level_up():
    global activeuser
    levelingup=True
    while levelingup==True:
        print("These are your creatures:")
        display_creatures()
        creature_levelingup=input("Which one do you want to level up?\nIf you don't want to level up any, type 'exit'.\n").capitalize()
        if creature_levelingup in activeuser["creatures"]:
                if activeuser["creatures"][creature_levelingup]["Xp"] >= activeuser["creatures"][creature_levelingup]["Xp_needed"]:
                        activeuser["creatures"][creature_levelingup]["damage"]+=7
                        activeuser["creatures"][creature_levelingup]["health"]+=5
                        activeuser["creatures"][creature_levelingup]["defense"]+=4
                        activeuser["creatures"][creature_levelingup]["Xp"]-=activeuser["creatures"][creature_levelingup]["Xp_needed"]
                        activeuser["creatures"][creature_levelingup]["Xp_needed"]+=50
                        activeuser["creatures"][creature_levelingup]["level"]+=1
                        print("You leveled up your %s!"%creature_levelingup)
                        levelingup=False
                else:
                    print("Not enough Xp!")
        elif creature_levelingup.lower()=="exit":
            break
        else:
            print("You don't have that creature!")

def daily_chest():
    global activeuser
    keep=True
    while keep:
        prizes=["xp","creature"]
        creatures=list(activeuser["creatures"])
        posibru_creatures=list(creature_database)
        random.shuffle(prizes)
        if prizes[0]=="xp":
            random.shuffle(creatures)
            xp=random.randint(10,int((activeuser["creatures"][creatures[0]]["level"]+.5))*35)
            activeuser["creatures"][creatures[0]]["Xp"]+=xp
            print("Your %s got %s xp from the daily chest!"%(creatures[0],xp))
            keep=False
        elif prizes[0]=="creature":
            if random.randint(0,1000)==1000:
                random.shuffle(possibru_creatures)
                print("You got a %s for the daily chest!"%posibru_creatures[0])
                add_creature(possibru_creatures[0])
                keep=False
    activeuser["daily_chest"]=time.time()

def add_creature(creature):
    global activeuser
    activeuser["creatures"][creature]=creature_database[creature]
    activeuser["creatures"][creature]["Xp"]=0
    activeuser["creatures"][creature]["Xp_needed"]=50
    activeuser["creatures"][creature]["level"]=1

def attack():
    global activeuser
    random.shuffle(creature_database_attributes)
    while True:
        print("These are your creatures:")
        display_creatures()
        attacking_creature=input("Which creature are you attacking with?\nIf you don't want to attack, type 'exit'.\n").capitalize()
        if attacking_creature in activeuser["creatures"]:
            break
        elif attacking_creature=="Exit":
            game()
        else:
            print("You don't have that creature!\n\n")
    anti_creature=creature_database_attributes[0]
    if random.randint(0,101)==100:
        print("It dosn't look like anyone is available right now. Please try again later")
    else:
        print("Looking for opponent...")
        time.sleep(random.randint(1,10))
    print("You are fighting a %s!"%anti_creature)
    first=random.randint(0,2)
    anti_creature_starting_health=creature_database[anti_creature]["health"]
    attacking_creature_starting_health=activeuser["creatures"][attacking_creature]["health"]
    if first==1:
        print("You go first!")
        keep=True
        while keep==True:
            for attack in activeuser["creatures"][attacking_creature]["attacks"]:
                print("\n%s:\n%s damage"%(attack,activeuser["creatures"][attacking_creature]["attacks"][attack]))
            attack=input("What attack do you use?\n").capitalize()
            if attack in activeuser["creatures"][attacking_creature]["attacks"]:
                keep=False
            else:
                print("Your creature doesn't have that attack!")
        if activeuser["creatures"][attacking_creature]["key_element"]==creature_database[anti_creature]["weakness"]:
            special_damage=creature_database[anti_creature]["weakness_level"]
        else:
            special_damage=0
        damage_dealt=(activeuser["creatures"][attacking_creature]["attacks"][attack]-creature_database[anti_creature]["defense"])+special_damage
        anti_creature_health=anti_creature_starting_health-damage_dealt
        print("You dealt %s damage! Their creature is at %s health!"%(damage_dealt,anti_creature_health))
        input("Press ENTER to continue\n")
        if activeuser["creatures"][attacking_creature]["Xp"]<0:
            activeuser["creatures"][attacking_creature]["level"]-=1
            activeuser["creatures"][attacking_creature]["Xp"]=0
        if activeuser["creatures"][attacking_creature]["level"]<=0:
            activeuser["creatures"][attacking_creature]["level"]=1
        while True:
            print("Their turn!")
            attacking_creature_health=activeuser["creatures"][attacking_creature]["health"]-0
            attacks=list(creature_database[anti_creature]["attacks"])
            anti_attack=creature_database[anti_creature]["attacks"][random.choice(attacks)]
            if creature_database[anti_creature]["key_element"]==activeuser["creatures"][attacking_creature]["weakness"]:
                anti_special_damage=activeuser["creatures"][attacking_creature]["weakness_level"]
            else:
                anti_special_damage=0
            attacking_creature_health=activeuser["creatures"][attacking_creature]["health"]
            anti_damage_dealt=(anti_attack-activeuser["creatures"][attacking_creature]["defense"])+anti_special_damage
            attacking_creature_health=attacking_creature_health-anti_damage_dealt
            if attacking_creature_health<0:
                attacking_creature_health=0
            elif anti_creature_health<0:
                anti_creature_health=0
            print("They dealt %s damage! Your creature is at %s health!"%(anti_damage_dealt,attacking_creature_health))
            input("Press ENTER to continue\n")
            if activeuser["creatures"][attacking_creature]["Xp"]<0:
                activeuser["creatures"][attacking_creature]["level"]-=1
                activeuser["creatures"][attacking_creature]["Xp"]=0
            if activeuser["creatures"][attacking_creature]["level"]<=0:
                activeuser["creatures"][attacking_creature]["level"]=1
            print("Your turn!")
            keep=True
            while keep==True:
                for attack in activeuser["creatures"][attacking_creature]["attacks"]:
                    print("\n%s:\n%s damage"%(attack,activeuser["creatures"][attacking_creature]["attacks"][attack]))
                attack=input("What attack do you use?\n").capitalize()
                if attack in activeuser["creatures"][attacking_creature]["attacks"]:
                    keep=False
                else:
                    print("Your creature doesn't have that attack!")
            if activeuser["creatures"][attacking_creature]["key_element"]==creature_database[anti_creature]["weakness"]:
                special_damage=creature_database[anti_creature]["weakness_level"]
            else:
                special_damage=0
            damage_dealt=(activeuser["creatures"][attacking_creature]["attacks"][attack]-creature_database[anti_creature]["defense"])+special_damage
            anti_creature_health=anti_creature_health-damage_dealt
            if attacking_creature_health<0:
                attacking_creature_health=0
            elif anti_creature_health<0:
                anti_creature_health=0
            print("You dealt %s damage! Their creature is at %s health!"%(damage_dealt,anti_creature_health))
            input("Press ENTER to continue\n")
            if activeuser["creatures"][attacking_creature]["Xp"]<0:
                activeuser["creatures"][attacking_creature]["level"]-=1
                activeuser["creatures"][attacking_creature]["Xp"]=0
            if activeuser["creatures"][attacking_creature]["level"]<=0:
                activeuser["creatures"][attacking_creature]["level"]=1
            if attacking_creature_health==0:
                print("Your creature lost. It lost 5 xp. It now has %s Xp."%activeuser["creatures"][attacking_creature]["Xp"]-5)
                activeuser[attacking_creature]["Xp"]-=5
                game()
            elif anti_creature_health==0:
                print("Your creature won! It gained 5 xp! It now has %s Xp!"%activeuser["creatures"][attacking_creature]["Xp"]+5)
                activeuser["creatures"][attacking_creature]["Xp"]+=5
                game()
            if activeuser["creatures"][attacking_creature]["Xp"]<0:
                activeuser["creatures"][attacking_creature]["level"]-=1
                activeuser["creatures"][attacking_creature]["Xp"]=0
            if activeuser["creatures"][attacking_creature]["level"]<=0:
                activeuser["creatures"][attacking_creature]["level"]=1
    else:
        print("The opponent goes first.")
        attacking_creature_health=attacking_creature_starting_health
        anti_creature_health=anti_creature_starting_health
        attacks=list(creature_database[anti_creature]["attacks"])
        anti_attack=creature_database[anti_creature]["attacks"][random.choice(attacks)]
        if activeuser["creatures"][attacking_creature]["key_element"]==creature_database[anti_creature]["weakness"]:
            anti_special_damage=creature_database[anti_creature]["weakness_level"]
        else:
            anti_special_damage=0
        anti_damage_dealt=(anti_attack-activeuser["creatures"][attacking_creature]["defense"])+anti_special_damage
        print("They dealt %s damage! Your creature is at %s health!"%(anti_damage_dealt,attacking_creature_health))
        input("Press ENTER to continue\n")
        if activeuser["creatures"][attacking_creature]["Xp"]<0:
            activeuser["creatures"][attacking_creature]["level"]-=1
            activeuser["creatures"][attacking_creature]["Xp"]=0
        if activeuser["creatures"][attacking_creature]["level"]<=0:
            activeuser["creatures"][attacking_creature]["level"]=1
    while True:
        print("Your turn!")
        keep=True
        while keep==True:
            for attack in activeuser["creatures"][attacking_creature]["attacks"]:
                print("\n%s:\n%s damage"%(attack,activeuser["creatures"][attacking_creature]["attacks"][attack]))
            attack=input("What attack do you use?\n").capitalize()
            if attack in activeuser["creatures"][attacking_creature]["attacks"]:
                keep=False
            else:
                print("Your creature doesn't have that attack!")
        if activeuser["creatures"][attacking_creature]["key_element"]==creature_database[anti_creature]["weakness"]:
            special_damage=creature_database[anti_creature]["weakness_level"]
        else:
            special_damage=0
        damage_dealt=(activeuser["creatures"][attacking_creature]["attacks"][attack]-creature_database[anti_creature]["defense"])+special_damage
        anti_creature_health-=damage_dealt
        if attacking_creature_health<0:
            attacking_creature_health=0
        elif anti_creature_health<0:
            anti_creature_health=0
        print("You dealt %s damage! Their creature is at %s health!"%(damage_dealt,anti_creature_health))
        input("Press ENTER to continue\n")
        if activeuser["creatures"][attacking_creature]["Xp"]<0:
            activeuser["creatures"][attacking_creature]["level"]-=1
            activeuser["creatures"][attacking_creature]["Xp"]=0
        if activeuser["creatures"][attacking_creature]["level"]<=0:
            activeuser["creatures"][attacking_creature]["level"]=1
        print("Their turn!")
        attacks=list(creature_database[anti_creature]["attacks"])
        anti_attack=creature_database[anti_creature]["attacks"][random.choice(attacks)]
        if creature_database[anti_creature]["key_element"]==activeuser["creatures"][attacking_creature]["weakness"]:
            anti_special_damage=activeuser["creatures"][attacking_creature]["weakness_level"]
        else:
            anti_special_damage=0
        anti_dammage_dealt=(anti_attack-activeuser["creatures"][attacking_creature]["defense"])+anti_special_damage
        attacking_creature_health=attacking_creature_health-anti_damage_dealt
        if attacking_creature_health<0:
            attacking_creature_health=0
        elif anti_creature_health<0:
            anti_creature_health=0
        print("They dealt %s damage! Your creature is at %s health!"%(anti_damage_dealt,attacking_creature_health))
        input("Press ENTER to continue\n")
        if attacking_creature_health==0:
            print("Your creature lost. It lost 5 xp. It now has %s X."%activeuser["creatures"][attacking_creature]["Xp"]-5)
            activeuser["creatures"][attacking_creature]["Xp"]-=5
            game()
        elif anti_creature_health==0:
            print("Your %s won! It gained 5 xp! It now has %s Xp!"%(attacking_creature,int(activeuser["creatures"][attacking_creature]["Xp"])+5))
            activeuser["creatures"][attacking_creature]["Xp"]+=5
            game()
        if activeuser["creatures"][attacking_creature]["Xp"]<0:
            activeuser["creatures"][attacking_creature]["level"]-=1
            activeuser["creatures"][attacking_creature]["Xp"]=0
        if activeuser["creatures"][attacking_creature]["level"]<=0:
            activeuser["creatures"][attacking_creature]["level"]=1
creature_database = {
    "Rocky":{
        "health":19,
        "defense":14,
        "key_element":"rock",
        "weakness":"wind",
        "weakness_level":3,
        "attacks":{
            "Boulder throw":15,
            "Rock smash":12,
            "Sonic clap":14
            }
        },

    "Flamdring":{
        "health":21,
        "defense":12,
        "key_element":"fire",
        "weakness":"water",
        "weakness_level":5,
        "attacks":{
            "Fire ball":16,
            "Solar summons":18,
            "Burst of flame":15
            }
        }

    }

creature_database_attributes=list(creature_database)

def play():
    activeuser = None
    log_on()
    intro()
    game()

play()
