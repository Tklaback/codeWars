"""
Author: Ty Klabacka

There exists a transformation, which brings equal symbols closer together, 
it is called the Burrows-Wheeler-Transformation. The forward transformation 
works as follows: Let's say we have a sequence with length n, first write every 
shift of that string into a n x n matrix:

Input: "bananabar"

b a n a n a b a r
r b a n a n a b a
a r b a n a n a b
b a r b a n a n a
a b a r b a n a n
n a b a r b a n a
a n a b a r b a n
n a n a b a r b a
a n a n a b a r b

Then we sort that matrix by its rows. The output of the transformation then 
is the last column and the row index in which the original string is in:

               .-.
a b a r b a n a n
a n a b a r b a n
a n a n a b a r b
a r b a n a n a b
b a n a n a b a r <- 4
b a r b a n a n a
n a b a r b a n a
n a n a b a r b a
r b a n a n a b a
               '-'

Output: ("nnbbraaaa", 4)
Of course we want to restore the original input, therefore you get the following hints:

The output contains the last matrix column.
The first column can be acquired by sorting the last column.
For every row of the table: Symbols in the first column follow on 
symbols in the last column, in the same way they do in the input string.
You don't need to reconstruct the whole table to get the input back.
Goal

The goal of this Kata is to write both, the encode and decode functions. 
Together they should work as the identity function on lists. 
(Note: For the empty input, the row number is ignored.)
"""

def encode(s):
    if s == "":
        return ("", 0)
    letterLyst = [letter for letter in s]
    
    appendLyst = []
    
    for num in range(len(letterLyst)):
        strang = ''.join([element for element in letterLyst])
        letterLyst.insert(0, letterLyst.pop())
        appendLyst.append(strang)
    appendLyst.sort()
    
    strang2 = ''.join([element[-1] for element in appendLyst])
    
    for number in range(len(appendLyst)):
        if appendLyst[number] == s: return (strang2, number)

def decode(s,n):
    letterLyst = [let for let in s] 
    
    sortedLetters = sorted(letterLyst) 
    
    sortedLyst, lyst = [], []
    sortedDyct, dyct = {}, {}
    
    for element in sortedLetters: 
        if element in sortedDyct: sortedDyct[element] += 1
        else: sortedDyct[element] = 0
    
    for element in letterLyst:
        if element in dyct: dyct[element] += 1
        else:dyct[element] = 0
    
    for item in sortedLetters:
        if item in sortedDyct:
            sortedLyst.append((item, sortedDyct[item]))
            sortedDyct[item] -= 1
    
    for item in letterLyst:
        if item in dyct:
            lyst.append((item, dyct[item]))
            dyct[item] -= 1
    
    first = sortedLyst[n]
    new_lyst = [first]
    while lyst:
        #start rebuilding the original word
        index = lyst.index(first)
        popped = sortedLyst.pop(index)
        new_lyst.append(popped)
        lyst.pop(index)
        first = popped
    new_lyst.pop()
    return ''.join([element[0] for element in new_lyst])