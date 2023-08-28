H,M,S,T=map(int,input().split())
t=(H*3600+M*60+S+T*5400)%129600
H=t//3600
M=(t-H*3600)//60
S=t-H*3600-M*60
print(f"{H}:{M:02d}:{S:02d}")
