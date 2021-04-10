# SPOJ question
import heapq
nodes,edges=list(map(int,input().split()))
graph=[[] for _ in range(nodes)]
ans=[]
heap=[]
enter=[0]*nodes
for _ in range(edges):
    u,v=list(map(int,input().split()))
    graph[u-1]+=[v]
    enter[v-1]+=1


for x in range(nodes):
    if enter[x]==0:
        heapq.heappush(heap,x+1)

while heap:
    curr=heapq.heappop(heap)
    ans.append(curr)
    for child in graph[curr-1]:
        enter[child-1]-=1
        if enter[child-1]==0:
            heapq.heappush(heap,child)


if len(ans)==nodes:
    print(ans)
else:   print("Sandro fails.")



