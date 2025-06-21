s1=input()
s2=input()

m,n=len(s1),len(s2)
prep=[0]*(n+1)
curr=[0]*(n+1)
res=0
for i in range(1,m+1):
    for j in range(1,n+1):
        if s1[i-1]==s2[j-1]:
            curr[j]=prep[j-1]+8
            res=max(res,curr[j])
        else:
            curr[j]=max(0,prep[j-1]-5,prep[j]-3,curr[j-1]-3)
    prep,curr=curr,prep
print(res)
