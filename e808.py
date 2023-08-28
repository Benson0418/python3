n=int(input())
h,m=map(int,input().split())
N=[]
for i in range(n):N.append(int(input()))
I=[int(x) for x in input().split()]
I.pop()
t=h*60+m
S=[t]
for i in range(n):
    S.append((S[i]+N[i])%1440)
for i in I:
    a=S[i]//60
    b=S[i]-a*60
    print(f"{a:02d}:{b:02d}")

