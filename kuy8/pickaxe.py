def stone_pick(arr):

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
