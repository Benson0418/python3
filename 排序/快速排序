def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


import random,time

test=[random.randint(1,100000) for _ in range(10000)]
a=time.time()
test=quick_sort(test)
b=time.time()
print(test==sorted(test))
print(f"time: {b-a:.6f}")
