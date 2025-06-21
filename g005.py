S=input()
L=[]
Lo=['+']
temp=[]
for i in S:
    if i=='+' or i=='-':
        L.append(temp)
        Lo.append(i)
        temp=[]
    else:
        temp.append(i)
L.append(temp)
temp=[]
for i in zip(L,Lo):
    if i[1]=='-':
        print(*i[0][::-1],sep='',end='')
    else:
        print(*i[0],sep='',end='')
