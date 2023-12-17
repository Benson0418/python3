class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        L = defaultdict(str)

        def find(x):
            if L[x]=='':
                L[x]=x
                return L[x]
            elif L[x]!=x:
                L[x]=find(L[x])
            return L[x]

        def union(a, b):
            pa,pb=find(a),find(b)
            if pa<pb:
                L[pb]=L[pa]
            else:
                L[pa]=L[pb]
        
        for i in range(len(s1)):
            union(s1[i], s2[i])

        result = []
        for char in baseStr:
            result.append(find(char))

        return ''.join(result)
