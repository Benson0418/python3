N=input()
L=[0]*26
for i in N:
    L[ord(i)-65]+=1
X=[]
for i in range(len(L)):
    if L[i] !=0:
        X.append([i,L[i]])
sX=sorted(X, key=lambda X:(-X[1],X[0]))
for i in sX:
    print(chr(i[0]+65),end='')
    
