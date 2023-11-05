from collections import deque
queue=deque()
n=int(input())
for _ in range(n):
    k,*l=map(int,input().split())
    if k==1:
        queue.append(l[0])
    elif k==2:
            print(queue[0] if queue else -1)
    elif queue:
        queue.popleft()

