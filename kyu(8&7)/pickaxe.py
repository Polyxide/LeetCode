"""
https://www.codewars.com/kata/65c0161a2380ae78052e5731/train/python
"""

#best solution

def stone_pick(arr):
    stick = arr.count('Sticks') + arr.count('Wood')*4
    cobble = arr.count('Cobblestone')
    return (min(cobble//3, stick//2))




#my solution

def stone_pickk(arr):

    sticks_counter = 0
    stones_counter = 0
    result = 0

    for x in arr:

        if x == 'Sticks':
            sticks_counter += 1

        elif x == 'Cobblestone':
            stones_counter += 1

        elif x == 'Wood':
            sticks_counter += 4

        else:
            pass

    while sticks_counter >= 2 and stones_counter >= 3:
        result += 1
        sticks_counter -= 2
        stones_counter -= 3

    return result
