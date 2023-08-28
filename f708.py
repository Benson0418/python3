M,N=map(int,input().split())
Ml=[int(x) for x in input().split()]
Nl=[int(x) for x in input().split()]
if M>N and sum(Ml)>sum(Nl):
    print("Yes")
else:
    print("No")
