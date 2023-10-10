from heapq import heapify,heappush,heappop
time=0
max_heap=[]
n=int(input())
L=sorted([[int(x) for x in input().split()]for _ in range(n)],key=lambda x:x[1]) # O(nlogn)
for dur,ddl in L: 
    if time+dur<=ddl:
        time+=dur
        heappush(max_heap,-dur) # O(n*logn)
    elif max_heap and -max_heap[0] > dur:
        time+=dur+heappop(max_heap)
        heappush(max_heap,-dur)
print(len(max_heap))

'''
時間複雜度: O(nlogn)
L傳入時間段和截止時間，並對截止時間排序
對於L中的每個持續時間即結束時間
  如果當前時間加上持續時間小於截止時間
    將當前時間更新，並將持續時間入隊
  否則如果當前隊列不為空且當中的最大持續時間大於新時間
    目前時間加上新的時間，
    減去堆中最大持續時間(由於是最大堆，所以取負號負負得正)
    舊的持續時間出隊，新的持續時間時間入隊
打印堆的長度
'''
