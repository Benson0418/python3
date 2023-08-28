n=int(input())
list_=[]
final_list=[]
for i in range(n):
    list_.append([int(x) for x in input().split()])
for i in range(0,n,2):
    temp_list=[]
    for j in range(0,n,2):
        temp_list.append(max(list_[i][j],list_[i][j+1],list_[i+1][j],list_[i+1][j+1]))
    final_list.append(temp_list)
for i in final_list:
    print(*i)
