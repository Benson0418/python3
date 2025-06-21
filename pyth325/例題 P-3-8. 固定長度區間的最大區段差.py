from collections import deque

n,k=map(int,input().split())
L=[int(x) for x in input().split()]
max_mono_queue=deque()
min_mono_queue=deque()

for i in range(k):
    while max_mono_queue and max_mono_queue[-1][0]<=L[i]:
        max_mono_queue.pop()
    max_mono_queue.append((L[i],i))
    while min_mono_queue and min_mono_queue[-1][0]>=L[i]:
        min_mono_queue.pop()
    min_mono_queue.append((L[i],i))
    
res=max_mono_queue[0][0]-min_mono_queue[0][0]

for right in range(k,n):
    left=right-k
    if max_mono_queue[0][1]==left:
        max_mono_queue.popleft()
    if min_mono_queue[0][1]==left:
        min_mono_queue.popleft()
    while max_mono_queue and max_mono_queue[-1][0]<=L[right]:
        max_mono_queue.pop()
    max_mono_queue.append((L[right],right))
    while min_mono_queue and min_mono_queue[-1][0]>=L[right]:
        min_mono_queue.pop()
    min_mono_queue.append((L[right],right))
    res=max(res,max_mono_queue[0][0]-min_mono_queue[0][0])

print(res)
