while True:
    try:
        n=int(input())
    except EOFError:
        break
    l=sorted([int(x) for x in input().split()])
    sorted_l=[]
    final=[]
    temp=[[]for _ in range(10)]
    for i in range(10):
        for j in l:
            if j%10==i:
                temp[i].append(j)
    for i in range(10):
        temp[i].reverse()
    for k in temp:
        final=final+k
    print(*final)
