X_1=[int(x) for x in input().split()]
X_2=[int(x) for x in input().split()]
n=int(input())
max_total=-10000
for i in range(n+1):
    max_total=max(max_total,X_1[0]*i*i+X_1[1]*i+X_1[2]+X_2[0]*(n-i)*(n-i)+X_2[1]*(n-i)+X_2[2])
print(max_total)
