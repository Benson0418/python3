class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def backtracking(curr,path):
            if not curr:
                res.append(path)
                return
            for i in range(len(curr)):
                l,r=0,i
                flag=False
                while l<r:
                    if curr[l]!=curr[r]:
                        flag=True
                        break
                    l+=1
                    r-=1
                if flag:
                    continue
                npath=path.copy()
                npath.append(curr[:i+1])
                backtracking(curr[i+1:],npath)   
        backtracking(s,[])    
        return res         
