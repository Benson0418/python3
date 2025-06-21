import random

def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot=arr[0]
    left=[]
    right=[]
    for i in range(1,len(arr)):
        if arr[i]<pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left)+[pivot]+quick_sort(right)
    





random_numbers = [random.randint(1, 100) for _ in range(10)]
print("原始數列:", random_numbers)


sorted_numbers = quick_sort(random_numbers)
print("排序後數列:", sorted_numbers)
