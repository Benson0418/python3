N=input()
M=[0]*10
T=[]
for i in N:
    M[int(i)]+=1
for i in range(10):
    if M[i]!=0:
        T.append((i,M[i]))
sT=sorted(T, key=lambda x: (-x[1], x[0]))
for i in sT:
    print(i[0],end=" ")

