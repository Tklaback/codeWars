"""
Author: Ty Klabacka

Functionality: function accepts an array of intervals, 
and returns the sum of all the interval lengths. 
Overlapping intervals should only be counted once.
"""
def sum_of_intervals(intervals):
    lyst = [number for ranges in intervals for number in range(ranges[0], ranges[1])]
    return len(list(set(lyst)))



print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
print(sum_of_intervals([(1, 5)]))
print(sum_of_intervals([(1, 5), (6, 10)]))