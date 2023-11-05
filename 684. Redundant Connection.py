class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def find(node):
            if parent[node]==node:
                return node
            parent[node]=find(parent[node])
            return parent[node]

        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1<p2:
                parent[p2]=p1
            else:
                parent[p1]=p2
            return

        n=len(edges)
        parent=[i for i in range(n+1)]
        for u,v in edges:
            ru,rv=find(u),find(v)
            if ru==rv:
                return [u,v]
            union(u,v)
