'''
https://www.codewars.com/kata/58dced7b702b805b200000be
'''

def distance_between_points(a, b):
    q = (a.x - b.x)**2
    p = (a.y - b.y)**2

    return float(((q + p)**(1/2)))