"""
Author: Ty Klabacka

Given an n x n array, return the array elements arranged 
from outermost elements to the middle element, traveling 
clockwise.The idea is not sort the elements from the lowest 
value to the highest; the idea is to traverse the 2-d array 
in a clockwise snailshell pattern.
"""

def snail(snail_map):
    lyst = []
    switch = -1
    if snail_map[0]:
        for num in range(len(snail_map) - 1):
            lyst.extend(num for num in snail_map[0])
            snail_map.pop(0)
            for lst in snail_map:
                lyst.append(lst.pop(switch))
            snail_map.reverse()
            if num % 2 == 0:
                snail_map[0].reverse()

            if num % 2 == 0: switch = 0
            else: switch = -1
        lyst.append(snail_map[0][0])
        return lyst
    return []



array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print(snail(array))
array = [[1,2,3,1],
         [4,5,6,4],
         [7,8,9,7],
         [7,8,9,7]]
snail(array)