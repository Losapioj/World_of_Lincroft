# Name: creature.py
# Final Project
# Creature Class
# Rob Casale, Chase, Matt Kahrer, Steve S
# Initial Submission

# Revision: ST 12/10/2013 - added getMaxHealth() and getHealth()
# Revision: JL 12/16/2013
#   - fix dealsDamage to actually do damage to an enemy, not self...
#   - added initialize for _thinMints and a getThinMints()
#   - fix minor bug in isDead()
#   - added returns to isDead()
#   - added self to dealsDamage(self)

import random

random.seed(None)

class Creature(object):

# Private Data Members
# _id (str), _maxHealth (int), _living (bool), _currHealth (int),
# _hitChance (int), _injury (int),
# _thinMints (int) (or should I say, Thin Ints?! *cricket*)

    def __init__(self):
        INJURY_DIE = 4

        self.setMaxHealth()
        
        self._currHealth = self._maxHealth
        self._id = ""
        self._injury = random.randint(1, INJURY_DIE)
        self._living = True
        self._thinMints = 0

    def __str__(self):
        print str(self._currHealth)
        print str(self._injury)

    def dealsDamage(self):
        return random.randint(1, 4)  

    def isDead(self):
        MIN_HEALTH = 1
        if self._currHealth < MIN_HEALTH:
            self._living = False
            return True
        else:
            self._living = True
            return False

    def isHit(self):
        self._hitChance = random.randint(0, 1)

        if self._hitChance == 0:
            return True
        else:
            return False

    def setMaxHealth(self):
        HEALTH_MAX = 12
        HEALTH_DIE = 4
        HEALTH_MOD = 3
        DROP = 1
        MIN_HEALTH = 1
        ROLL = 4

        tempStat = 0
        
        temp = []
        
        for INDEX in range(ROLL):
            temp.append(random.randint(1, HEALTH_DIE))

        for INDEX in range(DROP):
            temp.sort()
            temp.pop(0)

        for INDEX in range(len(temp)):
            tempStat += temp[INDEX]

        self._maxHealth = tempStat + HEALTH_MOD

        if self._maxHealth > HEALTH_MAX:
            self._maxHealth = HEALTH_MAX

    def takesHit(self, d):
        self._currHealth -= d

    def getHealth(self):
        return self._currHealth

    def setHealth(self, n):
        if n > self._maxHealth:
            n = self._maxHealth
        self._currHealth = n

    def getMaxHealth(self):
        return self._maxHealth

    def getThinMints(self):
        return self._thinMints

    def setThinMints(self, n):
        self._thinMints += n
