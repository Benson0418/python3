S,E,A=map(int,input().split())
D=1
while S<E and A>0:
    D+=1
    if D%9==1 or D%10==1:
        None
    elif D%3==1:
        S=S+S//3
    else:
        S=S+S//10
    if D%11==1:
        A-=1
if A<=0:
    print("unsalable")
else:
    print(D)
