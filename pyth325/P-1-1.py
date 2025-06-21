L=input().split()
idx=0
def find():
    global idx
    if L[idx]=='f':
        idx+=1
        a=find()
        return 2*a-1
    elif L[idx]=='g':
        idx+=1
        a=find()
        idx+=1
        b=find()
        return a+2*b-3
    else:
        return int(L[idx])

print(find())
