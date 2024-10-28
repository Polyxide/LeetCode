def highest_rank(arr):
    arr.sort()
    prev = None
    x = 0
    answer = 0
    for i in range(len(arr)):
        if prev == None:
            prev = arr[i]
            continue
        elif arr[i] == prev:
            if x < arr.count(arr[i]):
                x = arr.count(arr[i])
                answer = arr[i]
                prev = arr[i]
            elif x == arr.count(arr[i]):
                answer = (arr[i] if arr[i] > answer else answer)
                prev = arr[i]
            else:
                prev = arr[i]
                continue
        else:
            prev = arr[i]
            continue

    if answer == 0:
        return max(arr)
    elif answer == 0 and arr.count(0) > 0:
        return 0
    else:
        return answer



arr = [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]
print(highest_rank(arr))
