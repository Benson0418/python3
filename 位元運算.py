N=int(input())
nums=[int(x) for x in input().split()]
ones=twos=0
for num in nums:
    ones=(ones^num)&~twos
    twos=(twos^num)&~ones
print(ones)
