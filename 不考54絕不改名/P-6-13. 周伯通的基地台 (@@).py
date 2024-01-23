from collections import deque
mono_deque=deque()
mono_deque_idx=deque()

n,k=map(int,input().split())
C=[int(x) for x in input().split()]
dp=C[:k+1]+[0]*(n-k-1)
for i in range(k+1):
    while mono_deque and dp[i]<=mono_deque[-1]:
        mono_deque.pop()
        mono_deque_idx.pop()
    mono_deque.append(dp[i])
    mono_deque_idx.append(i)
for i in range(k+1,n):
    dp[i]=C[i]+mono_deque[0]
    while mono_deque and mono_deque_idx[0]<=i-(2*k+1):
        mono_deque.popleft()
        mono_deque_idx.popleft()
    while mono_deque and dp[i]<=mono_deque[-1]:
        mono_deque.pop()
        mono_deque_idx.pop()
    mono_deque.append(dp[i])
    mono_deque_idx.append(i)
print(min(dp[n-k-1:]))
