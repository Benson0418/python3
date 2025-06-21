N=int(input())
i=1
while N>4*i*(i+1)//2:i+=1
a=(4*i*(i+1)//2-N)//i
if a==0:
    print("Pineapple pen")
elif a==1:
    print("Apple")
elif a==2:
    print("Pineapple")
else:
    print("Pen")
