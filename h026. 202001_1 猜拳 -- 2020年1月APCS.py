F=int(input())
N=int(input())
list_N=[int(x) for x in input().split()]
list_F=[F,list_N[0]]+[0]*100
for i in range(2,N):
    if list_N[i-1]==list_N[i-2]:
        if list_N[i-1]==0:list_F[i]=5
        elif list_N[i-1]==2:list_F[i]=0
        else:list_F[i]=2
    else:list_F[i]=list_N[i-1]
count = 0
flag = True
for i in range(N):
    if list_F[i]==0 and list_N[i]==2 or list_F[i]==2 and list_N[i]==5 or list_F[i]==5 and list_N[i]==0:
        flag = False
        print(*list_F[:i+1],":","Won at round",i+1)
        break
    elif list_F[i]==0 and list_N[i]==5 or list_F[i]==2 and list_N[i]==0 or list_F[i]==5 and list_N[i]==2:
            flag = False
            print(*list_F[:i+1],":","Lost at round",i+1)
            break
if flag:print(*list_F[:i+1],":","Drew at round",N)
