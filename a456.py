for _ in range(int(input())):
    nums=[]
    result=[[]]
    n=int(input())
    for i in range(1,n+1):
        nums.append(i)
    for i in nums:
        new=[j+[i]for j in result]
        result.extend(new)
    result.sort(key=lambda x:[len(x),x])
    for i in result:
        if not i:
            print('{0}')
            continue
        else:
            print('{%s}'%','.join(map(str,i)))
    print()
