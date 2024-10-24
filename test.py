# def spatula(lst, poz):
#     lst.reverse()
#     return lst
#
# def biggest(lst):
#     index = 0
#     big = 0
#     for i in range(len(lst)):
#         if lst[i] > big:
#             big = list[i]
#             index = i
#     return index
#
#
# def flipper(lst):
#     new = lst.copy()
#     new1 = lst.copy()
#     new1.sort()
#     big = max(new)
#     answer = []
#
#     if new == sorted(new):
#         return new
#     elif big == (len(new)-1):
#         use1, use2 = flipper(new[:-1])
#         answer = use2
#         for i in range(len(use1)):
#             if new[i] == use1[i]:
#                 continue
#             else:
#                 new[i] = use1[i]
#
#         if new == new1:
#             return answer
#
#     elif big != 0:
#         spatula(new, big)
#         answer.append(big)
#         spatula(new, (len(new)-1))
#         answer.append((len(new)-1))
#     else:
#         new = spatula(new, (len(new) - 1))
#         answer.append((len(new) - 1))
#
#     if new == sorted(new):
#         returned = (new, answer)
#         return returned
#     else:
#         flipper(new)
#
#
# list = [2,1,2, 3, 5]
# # list1 = [1,5,8,3]
# print(flipper(list))
