class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        r_res=[]
        for i in strs:
            x=sorted(list(i))
            flag=True
            for idx,j in res:
                if x==j:
                    r_res[idx].append(i)
                    flag=False
            if flag:
                r_res.append([i])
                res.append((len(r_res)-1,x))
        return r_res
      
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L=defaultdict(list)
        for i in strs:
            L[''.join(sorted(i))].append(i)
        return L.values()
