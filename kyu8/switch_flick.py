"""
https://www.codewars.com/kata/64fbfe2618692c2018ebbddb/train/python
"""

# test


def flick_switch(lst):
    answer = []
    is_flicked = False

    for el in lst:
        if el == "flick":
            answer.append(is_flicked)
            is_flicked = not is_flicked
            continue
        answer.append(not is_flicked)

    return answer


myarray = ['codewars', 'flick', 'code', 'wars', 'flick', 'war']
print(flick_switch(myarray))