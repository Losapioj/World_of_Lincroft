#Version:
#   2 - fixed variable calls with self.
#   3 - added isHit() override from parent.

# Revision: JL 12/16/2013
#   - edited __str__ a bit

from creature import Creature

import random
random.seed(None)

# cookieMonster.py
# November 26, 2013
# Jeff Lasapio and David F. Rin

class CookieMonster(Creature):
#_xpValue, _thinMints, LEVEL1 = 60, LEVEL2 = 50, LEVEL3 = 40

    LEVEL1 = 60
    LEVEL2 = 50
    LEVEL3 = 40

    def __init__(self):
        super(CookieMonster, self).__init__()
        self._xpValue = random.randint(1, 3)
        self._thinMints = random.randint(self._xpValue, (2 * self._xpValue))

        if self._xpValue == 1:
            self._hitChance = CookieMonster.LEVEL1
        elif self._xpValue == 2:
            self._hitChance = CookieMonster.LEVEL2
        elif self._xpValue == 3:
            self._hitChance = CookieMonster.LEVEL3
            

    def __str__(self):
        str_msg = "You encounter a Cookie Monster \n" +\
                  "Cookie Monster: COOKIES!!!! ARRRHARRRA RAGH" +\
                  "\nHealth =" + str(super(CookieMonster, self).getHealth()) +\
                  "\nMax Health =" + str(super(CookieMonster, self).getMaxHealth()) +\
                  "\nxpValue =" + str(self._xpValue) +\
                  "\nI am am holding " + str(self._thinMints) +\
                  "Thin Mints"
        return str_msg

    def getXP(self):
        return self._xpValue

#    def getThinMints(self):
#        return self._thinMints

    def getHitChance(self):
        return self._hitChance

    def isHit(self):
        HIT_MAX = 100
        
        hitRate = random.randint(1, HIT_MAX)

        if hitRate <= self.getHitChance():
            return True

        return False
