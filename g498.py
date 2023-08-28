N,M,D=map(int,input().split())
flag=True
for i in range(0,D//N+1):
    for j in range(0,D//M+1):
        if i*N+j*M==D:
            print("YES")
            flag = False
            break
    if not flag:
        break
if flag:
    print("NO")
    
