'''
https://www.codewars.com/kata/598ee7b6ec6cb90dd6000061
'''


def count_repeats(txt):
    rep = 0
    prev = 0
    for i in txt:
        if i == prev:
            rep +=1
        prev = i
    return rep