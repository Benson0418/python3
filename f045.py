n=input()
n_l=[]
l=[]
for i in n:
    l.append(i)
n_l=[int(x) for x in l]
max_a=0
na=0
max_b=0
nb=0
for i in range(len(n_l)):
    if n_l[i]>max_a:
        max_a=n_l[i]
        na=i
n_l[na]=0
for i in range(len(n_l)):
    if n_l[i]>max_b:
        max_b=n_l[i]
        nb=i
if max_a**2+max_b**2==int(n)%1000:
    print("Good Morning!")
else:
    print("SPY!")
