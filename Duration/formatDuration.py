"""
Author: Ty Klabacka

This is a function which formats a duration, given as a number of 
seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just 
returns "now". Otherwise, the duration is expressed as a combination of 
years, days, hours, minutes and seconds.

Detailed rules:

The resulting expression is made of components like 4 seconds, 1 year, etc. 
In general, a positive integer and one of the valid units of time, separated 
by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last 
component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. 
Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated 
units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 
minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function 
should not return 61 seconds, but 1 minute and 1 second instead. Formally, the 
duration specified by of a component must not be greater than any valid more 
significant unit of time.
"""

def format_duration(seconds):
    if seconds == 0:
        return 'now'
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    years = days // 365
    if seconds >= 60: seconds %= 60
    if minutes >= 60: minutes %= 60
    if hours >= 24: hours %= 24
    if days >= 365: days %= 365
    dyct = {'years': years, 'days': days,
            'hours': hours, 'minutes': minutes,
            'seconds': seconds}
    strang = ''
    lyst = []
    for name, value in dyct.items():
        if value:
            if value == 1: lyst.append(f'{value} {name[:-1]}')
            else: lyst.append(f'{value} {name}')
    if len(lyst) == 1: return lyst[0]
    else:
        for item in lyst:
            if item == lyst[-2]:
                strang += lyst[-2] + ' and '
            elif item == lyst[-1]:
                strang += lyst[-1]
            else:
                strang += item + ', '
        return strang
