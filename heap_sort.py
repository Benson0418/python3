import random
import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    s_arr=[]
    while arr:
        s_arr.append(heapq.heappop(arr))
    return s_arr


random_numbers = [random.randint(1, 100) for _ in range(10)]
print("原始數列:", random_numbers)


sorted_numbers = heap_sort(random_numbers)
print("排序後數列:", sorted_numbers)
