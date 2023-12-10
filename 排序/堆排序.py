def heappush(arr,val):
    k=len(arr)
    arr.append(val)
    while k!=0 and arr[(k-1)//2]<arr[k]:
        arr[(k-1)//2],arr[k]=arr[k],arr[(k-1)//2]
        k=(k-1)//2
    return arr

def heapify1(arr): #下濾操作 O(n)
    k=(len(arr)-1)//2
    for i in range(k,-1,-1):
        k=i
        while 2*k+1<len(arr):
            if 2*k+2<len(arr) and arr[2*k+2]>arr[2*k+1]:
                if arr[k]<arr[2*k+2]:
                    arr[k],arr[2*k+2]=arr[2*k+2],arr[k]
                    k=2*k+2
                else:
                    break
            elif arr[k]<arr[2*k+1]:
                arr[k],arr[2*k+1]=arr[2*k+1],arr[k]
                k=2*k+1
            else:
                break

def heapify2(arr): #上濾操作 等於n次heappush O(nlogn)
    for i in range(len(arr)):
        k=i
        while k!=0 and arr[(k-1)//2]<arr[k]:
            arr[(k-1)//2],arr[k]=arr[k],arr[(k-1)//2]
            k=(k-1)//2
    return arr
                
def heappop(arr): #下濾操作
    arr[0],arr[-1]=arr[-1],arr[0]
    res=arr.pop()
    k=0
    while 2*k+1<len(arr):
        if 2*k+2<len(arr) and arr[2*k+2]>arr[2*k+1]:
            if arr[k]<arr[2*k+2]:
                arr[k],arr[2*k+2]=arr[2*k+2],arr[k]
                k=2*k+2
            else:
                break
        elif arr[k]<arr[2*k+1]:
            arr[k],arr[2*k+1]=arr[2*k+1],arr[k]
            k=2*k+1
        else:
            break
    return res

def heap_sort(arr,heapify): # 平均O(nlogn) 最壞O(nlogn) 最好O(nlogn)
    heapify(arr)
    i=len(arr)-1
    while i>=0:
        arr[0],arr[i]=arr[i],arr[0]
        k=0
        while 2*k+1<=i-1:
            child=2*k+1  # 使用 child 來表示左子節點
            if 2*k+2<=i-1 and arr[2*k+2]>arr[2*k+1]:
                child=2*k+2  # 如果右子節點更大，則更新 child
            if arr[k]<arr[child]:
                arr[k],arr[child]=arr[child],arr[k]
                k=child
            else:
                break
        i-=1


import random,time

test=[random.randint(1,100) for _ in range(10000)]
test2=test.copy()
a=time.time()
heap_sort(test,heapify1)
b=time.time()
heap_sort(test2,heapify2)
c=time.time()
print(test==sorted(test))
print(test2==sorted(test))
print(f"time: {b-a:.6f}")
print(f"time: {c-b:.6f}")


