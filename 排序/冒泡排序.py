def bubble_sort(arr):
    n = len(arr)
    flag = False
    for i in range(n-1, -1, -1):
        if flag:
            break
        flag = True
        for j in range(i):
            if arr[j] > arr[j+1]:
                flag = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


import random,time

test=[random.randint(1,100) for _ in range(10000)]
a=time.time()
bubble_sort(test)
b=time.time()
print(test==sorted(test))
print(f"time: {b-a:.6f}")
