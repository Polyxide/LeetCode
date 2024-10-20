from collections import deque




# '''
#
# Recursion:
#
# In case if a problem can be divided into smaller subproblems of the same type.
# Define base case, when recursion have to stop calling itself
# Define recursive case, where you are stating instructions which will apply each step
# (you have to call function itself here)
#
# '''



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













# '''
#
# Selection_sort /  O(n^2):
#
# In python just use .sort() method
#
# '''


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












# '''
#
# Quick_sort / O(n*log n):
#
# In python just use .sort() method
#
# '''


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











# '''
#
# Binary_search /  O(log n):
#
# In python just use .index() method
#
# '''


# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         guess = list[mid]
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








# '''
#
# Breadth-first_search / O(V + E):
#
# When there are several thing connected between each others
# and you need to find shortest connection between two of them
#
# '''


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










# '''
#
# Dijkstra's algorithm:
#
# If you have a path from A to B, where each step will cost you a points
#
# '''


# graph = dict()
#
# graph['start'] = dict()
# graph['start']['a'] = 5
# graph['start']['b'] = 2
#
# graph['a'] = dict()
# graph['a']['c'] = 4
# graph['a']['d'] = 2
#
# graph['b'] = dict()
# graph['b']['a'] = 8
# graph['b']['d'] = 7
#
# graph['c'] = dict()
# graph['c']['d'] = 6
# graph['c']['fin'] = 3
#
# graph['d'] = dict()
# graph['d']['fin'] = 1
#
# graph['fin'] = dict()
#
#
#
#
# infinity = float('inf')
# costs = dict()
# costs['a'] = 5
# costs['b'] = 2
# costs['c'] = infinity
# costs['d'] = infinity
# costs['fin'] = infinity
#
#
#
#
# parents = dict()
# parents['a'] = 'start'
# parents['b'] = 'start'
# parents['c'] = None
# parents['d'] = None
# parents['fin'] = None
#
#
# processed = []
#
#
#
# def find_lowest_cost_node(costs):
#
#     lowest_cost = float('inf')
#     lowest_cost_node = None
#
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#
#     return lowest_cost_node
#
#
#
# def Dijkstra(graph, costs, parents):
#
#     node = find_lowest_cost_node(costs)
#
#     while node is not None:
#         cost = costs[node]
#         neighbors = graph[node]
#         for n in neighbors.keys():
#             new_cost = cost + neighbors[n]
#             if costs[n] > new_cost:
#                 costs[n] = new_cost
#                 parents[n] = node
#         processed.append(node)
#
#
#         if node == 'fin':
#             processed.append(node)
#
#         node = find_lowest_cost_node(costs)
#
#
#     return costs['fin']
#
# shortest_path = Dijkstra(graph, costs, parents)
# print(shortest_path)













# '''
#
# Greedy Algorithms:
#
# If problem can be solved by making a series of locally optimal choices
# that lead to a globally optimal solution
#
# '''



#
# states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
#
# final_stations = set()
#
# stations = {}
# stations['kone'] = set(['id', 'nv', 'ut'])
# stations['ktwo'] = set(['wa', 'id', 'mt'])
# stations['kthree'] = set(['or', 'nv', 'ca'])
# stations['kfour'] = set(['nv', 'ut'])
# stations['kfive'] = set(['ca', 'az'])
#
#
# def greedy(states_needed, stations, final_stations):
#     while states_needed:
#         best_station = None
#         states_covered = set()
#
#         for station, regions in stations.items():
#             covered = states_needed & regions
#             if len(covered) > len(states_covered):
#                 best_station = station
#                 states_covered = covered
#
#         states_needed -= states_covered
#         final_stations.add(best_station)
#
#     print(final_stations)
#
# greedy(states_needed, stations, final_stations)











# '''
#
# Dynamic Programming:
#
#
#
# '''

# def knap_sack(dictionary, kg):
#
#     # dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1][0], reverse=True))
#
#     amount = 0
#     for i in dictionary.items():
#         amount += 1
#
#     dp = [[0]*(kg+1) for _ in range(amount+1)]
#
#     for i in range(1, amount+1):
#         weight, cost = list(dictionary.values())[i-1]
#         for j in range(1, kg+1):
#
#             if weight > j:
#                 dp[i][j] = dp[i - 1][j]
#             elif weight == j and dp[i-1][j] < cost:
#                 dp[i][j] = cost
#             elif weight == j and dp[i - 1][j] > cost:
#                 dp[i][j] = dp[i - 1][j]
#             elif j > weight:
#                 x = j - weight
#                 y = dp[i-1][x] + cost
#                 dp[i][j] = (y if y > dp[i-1][j] else dp[i-1][j])
#
#
#     return print(dp[amount][kg])
#
#
# items = dict()
# items['phone'] = [1, 2000]
# items['pods'] = [2, 2000]
# items['stereo'] = [4, 3000]
# items['laptop'] = [2, 2000]
# items['guitar'] = [1, 1500]
#
# max_weight = 6
#
# knap_sack(items, max_weight)







# def longest_common_substring(str1, str2):
#
#     m, n = len(str1), len(str2)
#
#
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
#     max_length = 0
#     ending_index = 0
#
#
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#                 if dp[i][j] > max_length:
#                     max_length = dp[i][j]
#                     ending_index = i
#             else:
#                 dp[i][j] = 0
#
#
#     return str1[ending_index - max_length: ending_index], max_length
#
#
#
# str1 = "blue"
# str2 = "clues"
# lcs, length = longest_common_substring(str1, str2)
# print(f"Longest Common Substring: '{lcs}' with length {length}")











# '''
#
# K-Nearest neighbors:
#
# If you have some points with several measured characteristics - you could find
# which from those points are closer to each other.   distance = sqrt( ((a1 - a2)**2) + ((b1 - b2)**2) ... )
#
# If those points with particular characteristics have any value assigned to them,
# you could define 'k' neighbors to one of them and avg of their value - will be the value of the one.
#
# '''
#