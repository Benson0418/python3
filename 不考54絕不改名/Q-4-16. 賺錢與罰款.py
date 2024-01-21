n=int(input())
T=[int(x) for x in input().split()]
D=[int(x) for x in input().split()]
M=sorted(list(zip(T,D)))

res=0
time=0
for i in range(n):
    time+=M[i][0]
    res+=M[i][1]-time
print(res)
