from bisect import bisect_left

n=int(input())
H=[0]+[int(x) for x in input().split()]
P=[0]+[int(x) for x in input().split()]
mono_stack=[]
mono_stack_idx=[]
count=0
for i in range(1,n+1):
    idx=bisect_left(mono_stack,-(H[i]+P[i]))
    if idx==0:
        count+=i-1
    else:
        count+=i-mono_stack_idx[idx-1]-1
    idx=bisect_left(mono_stack,-(H[i]))
    mono_stack[idx:]=[-(H[i])]
    mono_stack_idx[idx:]=[i]
print(count)
