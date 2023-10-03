di={'}':'{',']':'[',')':'('}
while True:
    try:
        n=input()
    except EOFError:
        break
    stack=[]
    flag=False
    for i in n:
        if i in di:
            if di[i]!=stack.pop():
                flag=True
                break
        else:
            stack.append(i)
    if flag or stack:
        print('no')
        continue
    print('yes')
        
        
