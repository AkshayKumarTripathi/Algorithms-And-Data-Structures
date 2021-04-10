# Single Source Shortest Path

nodes,edges = list(map(int,input().split()))

graph=[[] for _ in range(nodes)]

for _ in range(edges):
    a,b,w = list(map(int,input().split()))
    graph[a-1].append([b,w])
    graph[b-1].append([a,w])

import heapq

heap=[[0,1]]
ans=[-1]*nodes
while heap:
    dist,curr = heapq.heappop(heap)
    if ans[curr-1]!= -1 and ans[curr-1]<dist:
        continue

    elif ans[curr-1]==-1:
        ans[curr-1]=dist

    elif ans[curr-1]<dist:
        ans[curr-1]=dist

    for child in graph[curr-1]:
        to_dis=dist+child[1]
        if ans[child[0]-1]==-1 or ans[curr-1]>to_dis:
            heapq.heappush(heap,[to_dis,child[0]])

print(ans)