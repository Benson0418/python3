from bisect import bisect
n=int(input())
L=sorted([[int(x) for x in input().split()]for _ in range(n)])
L=[i[1] for i in L]
def LIS(s):
    sub=[]
    for i in s:
        idx=bisect(sub,i)
        if idx==len(sub):
            sub.append(i)
        else:
            sub[idx]=i
    return len(sub)
print(LIS(L))
