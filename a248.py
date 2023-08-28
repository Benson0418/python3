while True:
    try:
        a,b,n=map(int,input().split())
    except EOFError:
        break
    M=str(a//b)+'.'
    a=a%b
    N = str(a*10**n//b)
    if len(N)<n:
        N='0'*(n-len(N))+N
    print(M+N)
