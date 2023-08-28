L=[]
for i in range(3):
    L.append([int(x) for x in input().split()])
x=1
while True:
    if x%L[0][0]==L[0][1] and x%L[1][0]==L[1][1] and x%L[2][0]==L[2][1]:
        break
    x+=1
print(x)
