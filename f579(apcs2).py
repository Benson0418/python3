a,b=map(int,input().split())
n=int(input())
total=0
l = []
for i in range(n):
    l.append([int(x) for x in input().split()])
for i in l:
    ta=0
    tb=0
    for j in i:
        if j==a:ta+=1
        elif j==-a:ta-=1
        elif j==b:tb+=1
        elif j==-b:tb-=1
    if ta>0 and tb>0:
        total+=1
print(total)
    
