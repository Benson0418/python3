N=int(input())
S=[]
for i in range(N):
    S.append(int(input())%1000)
S.sort()
T=[0]*100
for i in S:
    T[i//10]+=1
for i in range(len(T)):
    if T[i]>0:
        print(i,T[i])
    
