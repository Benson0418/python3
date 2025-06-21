def f(n):
    if n==1:
        return 1
    return n*(n+1)//2
def g(n):
    if n==1:
        return 1
    return n*(n+1)*(2*n+1)/12+n*(n+1)/4
while True:
    try:
        n=int(input())
    except:
        break
    print(f(n),int(g(n)))
