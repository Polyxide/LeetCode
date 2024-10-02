from collections import deque



# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         guess = list[int(mid)]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
# my_list = [1, 3, 5, 7, 9, 11, 13]
#
# print(binary_search(my_list, 7))








# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr
#
# print(selectionSort([5, 3, 6, 2, 10]))






# counter = 0
# biggest = 0
# def recursive_sum(arr):
#     # Base case:
#     if len(arr) == 0:
#         return 0
#
#     # Recursive case:
#     global counter
#     counter += 1
#
#
#     global biggest
#     if arr[0] > biggest:
#         biggest = arr[0]
#
#
#     return arr[0] + recursive_sum(arr[1:])
#
# arra = [1, 2, 8, 4, 5, 3]
#
# print(recursive_sum(arra))
# print(counter)
# print(biggest)






# def binary_search(arr, target, low, high):
#
#     if low > high:
#         return None
#
#
#     mid = (low + high) // 2
#
#     if arr[mid] == target:
#         return mid
#     elif target < arr[mid]:
#         return binary_search(arr, target, low, mid - 1)
#     else:
#         return binary_search(arr, target, mid + 1, high)
#
# def search(arr, target):
#     return binary_search(arr, target, 0, len(arr) - 1)
#
#
# ar = [1, 2, 3, 4, 5, 6, 7]
# it = 6
#
# print(search(ar, it))






# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
#
# print(quicksort([10, 5, 2, 3]))








graph = dict()
graph['you'] = ['alex', 'vouva', 'roma']
graph['alex'] = ['katya', 'vlad']
graph['vouva'] = ['bohdan']
graph['roma'] = ['vlad', 'olya', 'katya']
graph['katya'] = []
graph['olya'] = []
graph['vlad'] = []
graph['bohdan'] = []


def person_is_seller(person):
    if person == 'bohdan':
        return True
    else:
        return False



def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False

search('you')