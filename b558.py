while True:
    try:
        n=int(input())
    except EOFError:
        break
    print(n*(n-1)//2+1)
