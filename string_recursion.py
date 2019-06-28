# CS5, hw1pr3
# Filename: hw1pr3.py
# Name:
# Problem description: Function Frenzy!

#
# leng example from class
#

#Given list L: [a, b, c, d, ...]
#Write a function that removes an element(s) from the list when function matches this format:
# removeAll(e, L)

def reverse(string):
    '''Takes a string as an argument and returns
       its reversal.'''
    if string == '':            # Is the string empty?
        return ''               # If so, reversing it is easy!
    else:
        firstSymbol = string[0] # Hold on to the first symbol
        return reverse(string[1:]) + firstSymbol