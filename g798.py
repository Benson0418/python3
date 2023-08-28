S=[int(x) for x in input().split()]
S.pop()
N=int(input())
for i in range(N):
    temp=[0]*len(S)
    for j in range(len(S)):
        if j==0:
            if S[0]>S[1]:
                temp[1]+=int(S[0]*0.1)
        elif j==len(S)-1 :
            if S[j]>S[j-1]:
                temp[j-1]+=int(S[j]*0.1)
        else:
            if S[j]>S[j-1]:
                temp[j-1]+=int(S[j]*0.05)
            if S[j]>S[j+1]:
                temp[j+1]+=int(S[j]*0.05)
    for j in range(len(S)):
        S[j]+=temp[j]
print(*S)
        
