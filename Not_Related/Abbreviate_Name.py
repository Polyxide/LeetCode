'''
https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
'''


def abbrev_name(name):
    answ = ''
    answ += name[0].upper()
    answ += '.'
    x = None
    for i in range(len(name)):
        if name[i] == ' ':
            answ += name[i+1].upper()
            break
    return answ