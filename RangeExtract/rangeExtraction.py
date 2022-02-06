"""
Author: Ty Klabacka

Description:
A format for expressing an ordered list of integers is 
to use a comma separated list of either

1. individual integers
2. or a range of integers denoted by the starting integer separated 
from the end integer in the range by a dash, '-'. The range includes 
all integers in the interval including both endpoints. It is not 
considered a range unless it spans at least 3 numbers. 
For example "12,13,15-17"

This function takes a list of integers in increasing order
and returns a correctly formatted string in the range format.
"""

def solution(args):
    master, lyst = [], []
    for number in range(len(args) -1):
        if args[number] + 1 == args[number + 1]: lyst.append(args[number])
        else:
            lyst.append(args[number])
            master.append(lyst)
            lyst = []
    master.append(lyst)
    print(master)
    if not master[-1]: master.pop()
    if master[-1][-1] + 1 == args[-1]: master[-1].append(args[-1])
    else: master.append([args[-1]])
    strang = f''
    for lst in master:
        if len(lst) >= 3:
            strang += f'{lst[0]}-{lst[-1]},'

        else:
            for item in lst:
                strang += f'{item},'
    return strang[:-1]
