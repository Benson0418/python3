def backtracking(s='',left=0,right=0):
    if len(s)==2*n:
        res.append(s)
        return
    if left<n:
        backtracking(s+'(',left+1,right)
    if right<left and left<=n:
        backtracking(s+')',left,right+1)
    return
while True:
    try:
        n=int(input())
    except EOFError:
        break
    res=[]
    backtracking()
    print('\n'.join(res))
    print()
