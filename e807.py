L=[]
for i in range(7):
    L.append([float(x) for x in input().split()])
maxD=0
D=0
for i in range(7):
    if sum(L[i])>maxD:
        maxD=sum(L[i])
        D=i
print(D+1)
maxE=0
E=0
for i in range(4):
    temp=0
    for j in range(7):
        temp+=L[j][i]
    if temp>maxE:
        maxE=temp
        E=i
if E==0:print("morning")
elif E==1:print("afternoon")
elif E==2:print("night")
else:print("early morning")
    
    
