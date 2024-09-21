def bubblesort(l):
    n = l
    for iteration in range(len(n)-1):
        for i in range(len(n)-1):
            if n[i] > n[i+1]:
                n[i], n[i + 1] = n[i + 1], n[i]
    return n

l = [9, 4, 2, 1, 3, 5, 8, 7, 6]

print(bubblesort(l))