from collections import deque



#                                                                              '''Recursion'''



# def recursive_sum(arr):
#
#     if len(arr) == 0:
#         return 0
#
#     return arr[0] + recursive_sum(arr[1:])
#
# arra = [1, 2, 8, 4, 5, 3]
#
# print(recursive_sum(arra))




# def binary_search(arr, target, low, high):
#
#     if low > high:
#         return None
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
#
#
# def search(arr, target):
#     return binary_search(arr, target, 0, len(arr) - 1)
#
#
# ar = [1, 2, 3, 4, 5, 6, 7]
# it = 6
#
# print(search(ar, it))





#                                                                             '''Selection_sort /  O(n^2)'''


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



#                                                                              '''Quick_sort / O(n*log n)'''


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




#                                                                              '''Binary_search /  O(log n) '''


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
# print(binary_search(my_list, 3))



#                                                                       '''Breadth-first_search / O(V + E)'''

# graph = dict()
# graph['you'] = ['alex', 'vouva', 'roma']
# graph['alex'] = ['katya', 'vlad']
# graph['vouva'] = ['bohdan']
# graph['roma'] = ['vlad', 'olya', 'katya']
# graph['katya'] = []
# graph['olya'] = []
# graph['vlad'] = []
# graph['bohdan'] = []
#
#
# def person_is_seller(person):
#     if person == 'bohdan':
#         return True
#     else:
#         return False
#
#
#
# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if not person in searched:
#             if person_is_seller(person):
#                 print(person + ' is a mango seller!')
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#
#     return False
#
# search('you')




#                                                                            '''Dijkstra's algorithm'''

#graph

graph = dict()

graph['start'] = dict()
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = dict()
graph['a']['fin'] = 1

graph['b'] = dict()
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = dict()


#costs

infinity = float('inf')
costs = dict()
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity


#parents

parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None


processed = []


#Algorithm

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def Dijkstra(graph, costs, parents):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
                processed.append(node)
        if node == 'fin':
            processed.append(node)
        node = find_lowest_cost_node(costs)
    return costs['fin']

shortest_path = Dijkstra(graph, costs, parents)
print(shortest_path)