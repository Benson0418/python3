N=int(input())
X=[int(x) for x in input().split()]
T=int(input())-1
while True:
    if T==0:
        if X[0]>X[1]:
            T=1
        else:break
    elif T==N-1:
        if X[T]>X[T-1]:
            T=T-1
        else:break
    else:
        if X[T]<X[T-1] and X[T]<X[T+1]:break
        else:
            if X[T]-X[T-1]>X[T]-X[T+1]:
                T-=1
            else:
                T+=1
print(T+1)
        
        
