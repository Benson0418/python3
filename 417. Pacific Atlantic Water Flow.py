class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights), len(heights[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        pacific=set()
        atlantic=set()
        queue=deque()
        for i in range(n):
            a,b=0,i
            if (a,b) in pacific:
                continue
            pacific.add((a,b))
            queue=deque([(a,b)])
            while queue:
                a,b=queue.popleft()
                for s,t in directions:
                    nx,ny=a+s,b+t
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in pacific and heights[nx][ny]>=heights[a][b]:
                        pacific.add((nx,ny))
                        queue.append((nx,ny))
        for i in range(1,m):
            a,b=i,0
            if (a,b) in pacific:
                continue
            pacific.add((a,b))
            queue=deque([(a,b)])
            while queue:
                a,b=queue.popleft()
                for s,t in directions:
                    nx,ny=a+s,b+t
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in pacific and heights[nx][ny]>=heights[a][b]:
                        pacific.add((nx,ny))
                        queue.append((nx,ny))
        for i in range(n):
            a,b=m-1,i
            if (a,b) in atlantic:
                continue
            atlantic.add((a,b))
            queue=deque([(a,b)])
            while queue:
                a,b=queue.popleft()
                for s,t in directions:
                    nx,ny=a+s,b+t
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in atlantic and heights[nx][ny]>=heights[a][b]:
                        atlantic.add((nx,ny))
                        queue.append((nx,ny))
        for i in range(m-1):
            a,b=i,n-1
            if (a,b) in atlantic:
                continue
            atlantic.add((a,b))
            queue=deque([(a,b)])
            while queue:
                a,b=queue.popleft()
                for s,t in directions:
                    nx,ny=a+s,b+t
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in atlantic and heights[nx][ny]>=heights[a][b]:
                        atlantic.add((nx,ny))
                        queue.append((nx,ny))
        res=[]
        if len(atlantic)<len(pacific):
            atlantic,pacific=pacific,atlantic
        for i in pacific:
            if i in atlantic:
                res.append(list(i))
        return res
        
