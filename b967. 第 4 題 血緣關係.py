from collections import deque
while True:
    try:
        n=int(input())
        L=[[] for _ in range(n)]
        for _ in range(n-1):
            p,c=map(int,input().split())
            L[p].append(c)
            L[c].append(p)
    except:
        break
    flag=[False]*(n)
    queue=deque()
    queue.append((0,0))
    res=[0]
    flag[0]=True
    while queue:
        node,count=queue.popleft()
        for i in L[node]:
            if not flag[i]:
                res.append(i)
                queue.append((i,count+1))
                flag[i]=True
    flag=[False]*(n)
    queue.append((res[-1],0))
    flag[res[-1]]=True
    res=0
    while queue:
        node,count=queue.popleft()
        for i in L[node]:
            if not flag[i]:
                queue.append((i,count+1))
                res=max(res,count+1)
                flag[i]=True
    print(res)
