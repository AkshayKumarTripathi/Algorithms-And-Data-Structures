# Creating Graph

nodes,edges=list(map(int,input().split()))
graph=[[] for _ in range(nodes)]
gnew=[[] for _ in range(nodes)]

for _ in range(edges):
    a,b,cost=list(map(int,input().split()))
    graph[a-1].append([b,cost])
    graph[b-1].append([a,cost])

import heapq
heap=[]
vis=set()
heap.append([0,4,-1])
c=0
while heap:
    cost,curr,where=heapq.heappop(heap)
    if curr in vis:
        continue
    vis.add(curr)
    c+=cost
    if where!=-1:
        gnew[where-1].append([curr,cost])
        gnew[curr-1].append([where,cost])
    
    for child in graph[curr-1]:
        if child[0] not in vis and child!=curr:
            heapq.heappush(heap,[child[1],child[0],curr])

for num,child in enumerate(gnew):
    print(num+1,child)
print(c)