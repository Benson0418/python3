import heapq
from sys import stdin
n = int(input())
grid = [[int(x) for x in stdin.readline().split()] for _ in range(n)]


def dijkstra(num):
    global n,grid
    dis = [[float('inf')]*n for _ in range(n)]
    dis[0][0] = 0
    visited = [[False]*n for _ in range(n)]
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    pq = [(0,0,0)]  # (distance, x, y)
    while pq:
        d,x,y = heapq.heappop(pq)
        if visited[x][y]: continue
        visited[x][y] = True
        for a,b in directions:
            r,s = x+a,y+b
            if 0<=r<n and 0<=s<n and abs(grid[r][s]-grid[x][y])<=num:
                if d+1 < dis[r][s]:
                    dis[r][s] = d+1
                    heapq.heappush(pq, (dis[r][s],r,s))
    return dis[n-1][n-1] if dis[n-1][n-1] != float('inf') else -1

left = 0
right = max(max(row) for row in grid)
while left < right: 
    mid = left + (right - left) // 2
    if dijkstra(mid) != -1:
        right = mid
    else:
        left = mid+1

distance = dijkstra(right)
print(right)
print(distance)
