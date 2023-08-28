K,W,S,E=map(int,input().split())
F=0
if K<=2:
    F+=20
else:
    F+=20+(K-2)*5
F+=W//2*5
if S<=18 and E>=19:
    F+=185
if S<=19 and E>=20:
    F+=195
if S<=20 and E>=21:
    F+=205
if S<=21 and E>=22:
    F+=215
if S<=22 and E>=23:
    F+=225
print(F)
