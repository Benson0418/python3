import random

def bubble_sort(arr):
    n=len(arr)
    flag=False
    for i in range(n-1,-1,-1):
        if flag:break
        flag=True
        for j in range(i):
            if arr[j]>arr[j+1]:
                flag=False
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

random_numbers = [random.randint(1, 100) for _ in range(10)]
print("原始數列:", random_numbers)


sorted_numbers = bubble_sort(random_numbers)
print("排序後數列:", sorted_numbers)

        
                
