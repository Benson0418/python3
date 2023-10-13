"""
對於要測試的數num，令變數
num-1=2^s*d，d為奇數、s為num-1質因數分解中2的最大個數
米勒-拉賓法告訴我們，若對於隨機挑選的憑證i，符合以下兩條件之一，則所測試的數極有可能為質數，而若不符合必為合數
i^d≡±1 (mod num)
i^(d*2^j)≡-1 (mod num) 其中j可為1~s-1中的任何數
經過前人長期觀察發現，對於int以下，憑證最多只需使用[2,7,61]即可完全避免偽質數產生
對於ull則最少需要以下八個數才能完全避免，不過一般不用保證100%嚴謹
"""
witness=[2,7,61]
# witness_ull=[2, 325, 9375, 28178, 450775, 9780504, 1795265022]
def isPrime(num):
    if num==1:
        return False
    if num==2:
        return True
    if ~num&1:
        return False
    if num==3:
        return True
    s=0
    d=num-1
    while ~d&1:
        s+=1
        d>>=1
    for i in witness:
        if i>=num:
            continue
        x=pow(i,d,num)
        if x==1 or x==num-1:
            continue
        flag=False
        for j in range(1,s):
            if pow(i,pow(2,j)*d,num)==num-1:
                flag=True
                continue
        if flag:
            continue
        return False
    return True
while True:
    o=int(input())
    if o==0:
        break
    print('質數' if isPrime(o) else '非質數')


    
