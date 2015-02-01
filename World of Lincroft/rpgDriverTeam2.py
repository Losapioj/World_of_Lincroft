# Team 2 rpgDriverTeam2.py
# Preliminary version 0.1

# Revision: JL 12/16/2013
#   - Game Loop first draft ->MAGIC STRINGS/NUMBERS ABOUND<-
#   - End of game messages
#   - Tested loop

from creature import Creature
from cookieMonster import CookieMonster
from customer import Customer

import random
random.seed()

DEBUG_MODE = True

def __main__():
    # create character
    myName = raw_input("Please enter character name: ")
    myGender = raw_input("Please enter character gender (M/F): ")
    if myName == "":
        myName = "Hero"
    if myGender =="":
        myGender ="M"
    myCustomer = Customer(myName, myGender)
    print str(myCustomer)

    myMonster = CookieMonster()
    print
    print str(myMonster)

    ###
    if DEBUG_MODE:
        print "DEBUG: cust/monst HP: " + str(myCustomer.getHealth()) +\
              "/" + str(myMonster.getHealth())
        print "DEBUG: DEATH: " + str(myCustomer.isDead()) +\
              "/" + str(myMonster.isDead())
    ###

    print "monster found! BATTLE!!"
    # while loop
    while ( not myCustomer.isDead() ) and myCustomer.getLevel() < 4:
        #if monster is alive
        #battle round
        if myMonster.getHealth() > 0:

            #####
            #USER TURN
            #####
            needInput = True
            monsterHit = False
            while needInput:

                print ""
                print "Your HP: " + str(myCustomer.getHealth()) +\
                      "Monster HP: " + str(myMonster.getHealth())
                print ""
                userIn = raw_input("would you like to (F)ight, " +\
                               "(R)un, or (E)xplode? ").upper()
                print ""
                if userIn == 'E':
                    print "You run up and hug the Cookie Monster, " +\
                          "begin to tick, and blow up, " +\
                          "taking it and all the thin mints with you."
                    myMonster.setHealth(0)
                    myCustomer.setHealth(0)
                    needInput = False
                    
                    ###
                    if DEBUG_MODE:
                        print "DEBUG: cust/monst HP: " + str(myCustomer.getHealth()) +\
                              "/" + str(myMonster.getHealth())
                        print "DEBUG: DEATH: " + str(myCustomer.isDead()) +\
                              "/" + str(myMonster.isDead())
                    ###
                        
                elif userIn == 'R':
                    print "COWARD! You manage to get away, "+\
                          "though not with your dignity..."
                    myMonster.setHealth(0)
                    needInput = False
                elif userIn == 'F':
                    monsterHit = True
                    print "You tell the Cookie Monster " +\
                          "you don't have any money!"
                    if myMonster.isHit():
                        dmg = myCustomer.dealsDamage()
                        print "You weaken the Cookie Monster's " +\
                              "sales pitch by " + str(dmg) + " damage!"
                        myMonster.takesHit(dmg)
                    else:
                        print "The Cookie Monster doesn't believe your lie " +\
                              "and laughs at your incompetence!"
                    needInput = False
                else:
                    print "Lets try this input thing again, shall we?"

            #####
            #MONSTER TURN
            #####
            #if monster is still alive
            if not myMonster.isDead():
                print "The Cookie Monster tries to sell you delicious cookies!"
                if myCustomer.isHit():
                    dmg = myMonster.dealsDamage()
                    print "The Cookie Monster hits your wallet for " +\
                          str(dmg) + " damage!"
                    myCustomer.takesHit(dmg)
                else:
                    print "You start to talk about the weather, " +\
                          "breaking the Cookie Monster's sales pitch!"
            #if monster was killed by player
            elif monsterHit:
                print "You chased her off crying! " +\
                      "\nDon't you feel like a big person!"

                #get XP
                myCustomer.setExperience(myMonster.getXP())
                myCustomer.incrementLevel()
                print "!!!LEVEL UP!!! \n*fireworks, fireworks*\n" +\
                      "You are now level " + str(myCustomer.getLevel())
                #get cookies
                cookiesDropped = myMonster.getThinMints()
                if cookiesDropped > 0:
                    print "Wait, she dropped some cookies! " +\
                          "Well, would be a shame if they went to waste..."
                    print "\nAcquired " + str(cookiesDropped) +\
                          " Cookies!\n"
                    myCustomer.setThinMints(cookiesDropped)



        #if monster is dead
        else:
            #regen
            if myCustomer.getHealth() < myCustomer.getMaxHealth():
                myCustomer.regenHealth()
            #eat cookies
            if myCustomer.getThinMints() != 0:
                print "You have " + str(myCustomer.getThinMints()) +\
                      "\nand " + str(myCustomer.getHealth()) +\
                      "/" + str(myCustomer.getMaxHealth()) +\
                      "health."
                userIn = eval(raw_input("How many thin mints would" +\
                                        "you like to eat? "))
                myCustomer.eatThinMints(userIn)
                print "You NOW have " + str(myCustomer.getThinMints()) +\
                      "\nand " + str(myCustomer.getHealth()) +\
                      "/" + str(myCustomer.getMaxHealth()) +\
                      "health."
                
            #chance to ATAMO
            if myCustomer.atamo():
                print "REMEMBER THE ALAMO! errr... ATAMO! " +\
                      "\n FULL HEAL!"
                myCustomer.setHealth(myCustomer.getMaxHealth())
                
            #chance to spawn new monster
            if random.randint(1, 3) == 1:
                myMonster = CookieMonster()
                print "monster found! BATTLE!!"

    #####
    #END GAME LOOP
    #DO END GAME RESULTS
    #####
    #end of game messages, check health and level to determine msg
    print "\n"
    if myCustomer.isDead():
        if myMonster.isDead():
            print "Well, you're in debt for the rest of your life, " +\
                  "but at least you took one down with you!"
        else:
            print "You have fallen to the seductive nature of the thin mint." +\
                  "Enjoy being broke and fat!"
    elif myMonster.isDead():
        if myCustomer.getLevel() >= 4:
            print "You Win!!! You weathered the storm and " +\
                  "managed to keep your bank account in the black... this year!"
        else:
            print "Wait, you shouldn't be here!" +\
                  "Quick! Report this bug to the nearest girlscout!!"

    print "\nGAME OVER\n"
    raw_input("Press Enter to exit.")
        

if __name__ == '__main__':
    __main__()
