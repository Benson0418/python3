n=int(input())
T=[int(x) for x in input().split()]
W=[int(x) for x in input().split()]
L=sorted([(T[i]/W[i],i) for i in range(n) if W[i]>0])

time=0
res=0
for _,i in L:
    time+=T[i]
    res+=W[i]*time
print(res)
    
    
