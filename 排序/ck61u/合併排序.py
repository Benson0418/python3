def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
    else:
        left = []
        right = []

    l = r = i = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr[i] = left[l]
            l += 1
        else:
            arr[i] = right[r]
            r += 1
        i += 1

    while l < len(left):
        arr[i] = left[l]
        l += 1
        i += 1
    while r < len(right):
        arr[i] = right[r]
        r += 1
        i += 1
        
    return arr


import random,time

test=[random.randint(1,100000) for _ in range(10000)]
a=time.time()
test=merge_sort(test)
b=time.time()
print(test==sorted(test))
print(f"time: {b-a:.6f}")
