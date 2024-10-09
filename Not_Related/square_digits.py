'''
https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
'''


def square_digits(num):
    num = str(num)
    str_list = []
    for i in range(len(num)):
        x = int(num[i]) ** 2
        str_list.append(str(x))

    collapsed_string = ''.join(str_list)
    return int(collapsed_string)

num = 1234

print(square_digits(num))