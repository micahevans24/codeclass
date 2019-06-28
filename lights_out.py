#
# hw3pr1.py - Lab problem: "Lights On!"
#
# Name:
#
#

import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.
import sys            # larger recursive stack
sys.setrecursionlimit(10000) # 10000 stack frames availble


def mutate(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = 1 + oldL[i]
    return new_ith_element

def rand(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = oldL[i]
    return choice([0,1])

def allOnes(L):
    if L == []:
        return True

    elif L[0] != 1:
        return False    
    
    else:
        return allOnes(L[1:])

assert allOnes([1,1,1]) == True
assert allOnes([]) == True
assert allOnes([0,0,2,2]) == False
assert allOnes([1,1,0]) == False


def toggle(i, oldL, target = 0):
    """ Accepts an index (i), an old list (oldL) and the index to turn on (target).
        toggle returns the ith element of a NEW list!
        * Note that toggle returns ONLY the ith element
          toggle thus needs to be called many times in evolve.
    """
    if i == target or i == target + 1 or i == target - 1:
        if oldL[i] == 0:
           new_ith_element = 1       # this makes the game easy!
        else: # oldL[i] == 1
           new_ith_element = 0
    else:
        new_ith_element = oldL[i] # the new is the same as the old
    return new_ith_element


def evolve(oldL, mutate, curgen = 0):
    """ This function should evolve oldL (a list)
        it starts at curgen, the "current" generation
        and it ends at generation #5 (for now)
        
        It works by calling mutate at each index i.
    """
    print (oldL)                    # print the old list, L
    print ("  (gen: " + str(curgen) + ")")  # and its gen.
    time.sleep(0.25)
    
    if allOnes(oldL):  # we're done!
        return curgen      # no return value... yet
    else:
        user = int(input("Index? "))
        newL = [ mutate(i,oldL,user) for i in range(len(oldL)) ]
        return evolve(newL, mutate, curgen + 1)

#calling

print(evolve([1,0,0,1,0,0,1,1], toggle))