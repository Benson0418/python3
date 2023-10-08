# x,y,p ∈ N
def quick_pow(x, y, p):
    res = 1
    while y > 0:
        if y & 1: # y % 2 == 1
            res = (res * x) % p
        y >>= 1 # y//=2
        x = (x * x) % p
    return res

x, y, p = map(int, input().split())
print(quick_pow(x, y, p))
