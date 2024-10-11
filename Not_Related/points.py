'''
https://www.codewars.com/kata/5bb904724c47249b10000131/train/python
'''


def points(games):
    points = 0
    for i in games:
        if int(i[0]) > int(i[2]):
            points += 3
        elif int(i[0]) == int(i[2]):
            points += 1
        else:
            pass
    return points

arr = ['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']
print(points(arr))