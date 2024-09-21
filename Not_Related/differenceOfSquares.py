"""
https://www.codewars.com/kata/558f9f51e85b46e9fa000025/train/python
"""


#best solution

def difference_of_squares(n):
    return sum(range(n+1))**2 - sum(i**2 for i in range(n+1))



#my solution

def difference_of_squaress(n):

    squareOfSum = 0
    sumOfSquares = 0

    for el in range(n + 1):
        squareOfSum += el

    for el in range(n + 1):
        sumOfSquares += el ** 2

    answer = squareOfSum ** 2 - sumOfSquares
    return answer

print(difference_of_squaress(5))



