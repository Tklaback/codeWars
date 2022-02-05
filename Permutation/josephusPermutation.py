"""
Author: Ty Klabacka

This is a function that returns a Josephus permutation, taking as parameters the initial 
array/list of items to be permuted as if they were in a circle and counted out 
every k places until none remained.
"""

def josephus(items,k):
    tracer = k-1
    lyst = []
    while items:
        if tracer >= len(items):
            tracer = (tracer % len(items))
        lyst.append(items.pop(tracer))
        tracer += k-1
    return lyst

