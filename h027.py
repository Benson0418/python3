s,t,n,m,r=map(int,input().split())
SL=[[int(x) for x in input().split()]for _ in range(s)]
BL=[[int(x) for x in input().split()]for _ in range(n)]
a=0
b=[]

for i in SL:a+=sum(i)
for i in range(n-s+1):
    for j in range(m-t+1):
        tr=r
        tb=0
        flag=False
        for k in range(s):
            for l in range(t):
                if SL[k][l]!=BL[i+k][j+l]:
                    tr-=1
                if tr<0:
                    flag=True
                    break
                tb+=BL[i+k][j+l]
            if flag:
                break
        if not flag:
            b.append(tb)
print(len(b))
if not b:
    print(-1)
else:
    bresult=2147483647
    for i in b:
        bresult=min(abs(i-a),bresult)
    print(bresult)
