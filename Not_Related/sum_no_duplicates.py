"""
https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2
"""

#best solution

def sum_no_duplicates(l):
    return sum(n for n in set(l) if l.count(n) == 1)



#my solution

def sum_no_duplicates1(l):
    sum = 0
    nums = []
    ban = []

    for el in range(len(l)):

        if (l[el] not in nums) and (l[el] not in ban):
            nums.append(l[el])
        elif l[el] in nums:
            nums.remove(l[el])
            ban.append(l[el])
        elif l[el] in ban:
            continue


    for iter in range(len(nums)):
        sum += nums[iter]

    return sum

per = [5, 6, 10, 3, 10, 10, 6, 7, 0, 9, 1, 1, 6, 3, 1]

print(sum_no_duplicates1(per))