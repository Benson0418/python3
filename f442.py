N=int(input())
C=[int(x) for x in input().split()]
E=int(input())
q=int(input())
Q=[int(x) for x in input().split()]
for i in range(q):
    for j in range(len(C)):
        if C[j]==Q[i]:
            C[j],E=E,C[j]
            break
print(*C)
