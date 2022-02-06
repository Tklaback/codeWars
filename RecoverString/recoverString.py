"""
Author: Ty Klabacka

Description:
There is a secret string which is unknown to you. Given a 
collection of random triplets from the string, recover the 
original string.

A triplet here is defined as a sequence of three letters 
such that each letter occurs somewhere before the next in 
the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs 
more than once in the secret string.

You can assume nothing about the triplets given to you 
other than that they are valid triplets and that they 
contain sufficient information to deduce the original string. 
In particular, this means that the secret string will never 
contain letters that do not occur in one of the triplets 
given to you.
"""

def remove(element, lyst):
    return [item for item in lyst if item != element]

def recoverSecret(triplets):
    lyst = [element for lst in triplets for element in lst]
    new_lyst = []
    while lyst:
        culprit = lyst[0]
        for lst in triplets:
            if culprit in lst and lst.index(culprit):
                if lst[0] not in new_lyst: culprit = lst[0]
                elif lst[1] not in new_lyst: culprit = lst[1]
        for lst in reversed(triplets):
            if culprit in lst and lst.index(culprit):
                if lst[0] not in new_lyst: culprit = lst[0]
                elif lst[1] not in new_lyst: culprit = lst[1]
        lyst = remove(culprit, lyst)
        new_lyst.append(culprit)
    return ''.join([word for word in new_lyst])

