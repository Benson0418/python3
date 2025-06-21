N,M,K=map(int,input().split())
t=0
m=0
while True:
    if K==0:
        if N<32 and t==0:
            print("Wayne can't eat and drink.")
            break
        N-=32
        if N==0:
            print(f"{m}: Wayne eats an Apple pie, and now he doesn't have money.")
            break
        elif N==1:
            print(f"{m}: Wayne eats an Apple pie, and now he has 1 dollar.")
            break
        print(f"{m}: Wayne eats an Apple pie, and now he has {N} dollars.")
        K=1
        m+=M
        if N<55:
            break
    if K==1:
        if N<55 and t==0:
            print("Wayne can't eat and drink.")
            break
        N-=55
        if N==0:
            print(f"{m}: Wayne drinks a Corn soup, and now he doesn't have money.")
            break
        elif N==1:
            print(f"{m}: Wayne drinks a Corn soup, and now he has 1 dollar.")
            break
        print(f"{m}: Wayne drinks a Corn soup, and now he has {N} dollars.")
        K=0
        m+=M
        if N<32:
            break
