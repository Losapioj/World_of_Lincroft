# Revisions: ST 12/10/2013
#   - revised gender to be "Male", "Female" or "Other"
#   - added from creature import Creature
#   - aded call to super in __init__()
#   - expanded __str__()
#   - deleted unused code
#   - added setLevel(), getLevel(),and incrementLevel() functions

# Revision: JL 12/16/2013
#   - fix regen to not pass _maxHealth
#   - fix all healing functions, can not call private data from parent
#   - added self. to all roll calls
#   - fix loop call in roll
#   - added self to all healing headers

from creature import Creature

import random
random.seed()

FACES = 4
MIN = 1
ROLLS = 4
#KEEPERS = 3
OFFSET = 0

class Customer(Creature):

    INIT_MSG1 = "My name is "
    INIT_MSG2 = "\nMy gender is "
    INIT_MSG3 = "\nMy level is "
    INIT_MSG4 = "\nMy health is "
    INIT_MSG5 = "\nMy max health is "

    def __init__(self, n, g):
        super(Customer, self).__init__()
        self._gender = self.__setCharGender(g)
        self._name = self.__setCharName(n)          
        self._curExperience = 0
        self._level = 1
        

    def __str__(self):
        str_msg = Customer.INIT_MSG1 + self._name + \
                  Customer.INIT_MSG2 + self._gender + \
                  Customer.INIT_MSG3 + str(self._level) + \
                  Customer.INIT_MSG4 + str(super(Customer, self).getHealth()) + \
                  Customer.INIT_MSG5 + str(super(Customer, self).getMaxHealth())
        
        return str_msg

    def roll(self, dice = ROLLS, face = FACES, offset = OFFSET):
        num = 0
        for rolls in range(dice):
            roll = random.randint(MIN, face)
            num += roll
        return num
    
 #################################Gender   
    def __setCharGender(self, g):
        if g == "m" or g == "M":
            self._gender = "Male"
        elif g == "f" or g == "F":
            self._gender = "Female"
        else:
            self._gender = "Other"

        return self._gender

    def setGender(self, g):

        self._gender = self.__setGender(g)

    def getGender(self):

        return self._gender
##################################Name
    def __setCharName(self, n):
        #print n
        if n == "":
            n = "Hero"
        return n

    def getName(self):
        
        return self._name

    def setName(self, n):
        
        self._name = self.__setCharName(n)

    def __setExperience(self, pExperience):
        ##experience loaded from save game
        ##pExp = previous experience

        self._curExperience += pExperience
    
    def getExperience(self):
        return self._curExperience

    def setExperience(self, nExperience):
        ##nExp = new exp
        self._curExperience += nExperience

    def getLevel(self):
        return self._level

    def setLevel(self, level):
        self._level = level
    
    def incrementLevel(self):
        self._level += 1

######################################ThinMints
    def eatThinMints(self, nMints):
        super(Customer, self).setThinMints(-nMints)
        if nMints > (super(Customer, self).getMaxHealth() - super(Customer, self).getHealth()):
            nMints = super(Customer, self).getMaxHealth() - super(Customer, self).getHealth()
        super(Customer, self).takesHit(-nMints)

######################################RegenHealth
    def regenHealth(self):
        super(Customer, self).takesHit( -(self.roll(2, 1)))
        if super(Customer, self).getHealth() > super(Customer, self).getMaxHealth():
            super(Customer, self).setHealth(super(Customer, self).getMaxHealth())

    def atamo(self):
        if (self.roll(1, 6) == 1):
            super(Customer, self).setHealth(super(Customer, self).getMaxHealth())
            return True
        else:
            return False
        
##################################Properties   
    nameParameter = property(getName, setName)
    levelParameter = property(getLevel, setLevel)
    expParameter = property(getExperience, setExperience)
