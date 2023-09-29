from collections import deque
from sys import stdin
n=int(stdin.readline())
grid=[[int(x) for x in stdin.readline().split()]for _ in range(n)]
times=0
def BFS(num):
    global n,grid,times
    times=1
    flag=[[-1]*n for _ in range(n)]
    queue=deque([(0,0)])
    flag[0][0]=0
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    while queue:
        x,y=queue.popleft()
        for a,b in directions:
            r,s=x+a,y+b
            if 0<=r<n and 0<=s<n and flag[r][s]==-1:
                if abs(grid[r][s]-grid[x][y])<=num:
                    queue.append((r,s))
                    flag[r][s]=flag[x][y]+1
        times+=1
    times=flag[n-1][n-1]
    return False if flag[n-1][n-1]==-1 else True
left=0
right=0
for i in range(n):
    for j in range(n):
        right=max(right,grid[i][j])
while left<right: 
    mid=left+(right-left)//2
    if BFS(mid):
        right=mid
    else:
        left=mid+1
BFS(right)
print(right)
print(times)
