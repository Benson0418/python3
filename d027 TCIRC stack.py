L=input()
nums=[]
ops=[]
num=0
op='+'
result=0
for i in L:
    if i.isdigit():
        num=num*10+int(i)
    else:
        if op=='*':
            nums.append(nums.pop()*num)
        elif op=='/':
            nums.append(nums.pop()//num)
        else:
            ops.append(op)
            nums.append(num)
        op=i
        num=0
if op=='*':
    nums.append(nums.pop()*num)
elif op=='/':
    nums.append(nums.pop()//num)
else:
    ops.append(op)
    nums.append(num)
for i in range(len(nums)):
    if ops[i]=='+':
        result+=nums[i]
    else:
        result-=nums[i]

print(result)
