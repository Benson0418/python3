import random
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)
    else:
        left=[]
        right=[]

    l=r=i=0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            arr[i]=left[l]
            l+=1
        else:
            arr[i]=right[r]
            r+=1
        i+=1

    while l<len(left):
        arr[i]=left[l]
        l+=1
        i+=1
    while r<len(right):
        arr[i]=right[r]
        r+=1
        i+=1

    return arr


random_numbers = [random.randint(1, 100) for _ in range(10)]
print("原始數列:", random_numbers)


sorted_numbers = merge_sort(random_numbers)
print("排序後數列:", sorted_numbers)

