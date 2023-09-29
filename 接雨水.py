height=[int(x) for x in input().split()]
n = len(height)
left,right=0,len(height)-1
left_max,right_max=height[left],height[right]
trapped_water =0
max_hight=0
move=0

while left < right:
    a,b=height[left]-max_hight,height[right]-max_hight
    if move==0:
        trapped_water-=min(max_hight,height[left])
    else:
        trapped_water-=min(max_hight,height[right])
    trapped_water+=max(min(height[left],height[right])-max_hight,0)*(right-left-1)
    max_hight=max(min(height[left],height[right]),max_hight)
    if height[left]<=height[right]:
        left+=1
        move=0
    else:
        right-=1
        move=1
print(trapped_water)
