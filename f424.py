n=int(input())
a,b=1,3
for i in range(3,n+1):
    b,a=a+b,b
print(b)
