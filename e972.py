m = input().replace('\r', ' ')
try:
    n = input()
except:
    m,a,b=m.split()
else:
    a,b=n.split()
a=int(a)
m=int(m)
if b=="T":
    y=m/1.0-a
elif b=="U":
    y=m/30.9-a
elif b=="J":
    y=m/0.28-a
else:
    y=m/34.5-a
if y<0:
    print("No Money")
elif y<0.05:
    print(b,"0.00")
else:
    print(b,"%.2f" %y)
