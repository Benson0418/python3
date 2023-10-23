witness= [2,7,61]
def isPrime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if ~n&1:
        return False
    if n==3 or n==5:
        return True
    s=0
    d=n-1
    while ~d&1:
        s+=1
        d>>=1
    for a in witness:
        if a>=n:
            continue
        x=pow(a,d,n)
        if x==1 or x==n-1:
            continue
        flag=False
        for s1 in range(1,s):
            x=pow(a,d*pow(2,s1),n)
            if x==n-1:
                flag=True
                break
        if flag:
            continue
        return False
    return True
for _ in range(int(input())):
    flag=True
    n=input()
    for i in range(7):
        if not isPrime(int(n[i:])):
            flag=False
            break
    if flag:
        print(f"{n} is a Prime Day!")
    else:
        print(f"{n} isn't a Prime Day!")
        

    
