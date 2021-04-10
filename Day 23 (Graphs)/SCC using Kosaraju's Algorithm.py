

nodes,edges=list(map(int,input().split()))

graph=[[] for _ in range(nodes)]
tgraph=[[] for _ in range(nodes)]

for _ in range(edges):
    a,b=list(map(int,input().split()))
    graph[a-1].append(b)
    tgraph[b-1].append(a)

vis=set()
tvis=set()

stack=[]
ans=[]
temp=[]

def dfs1(root):
    vis.add(root)
    for child in graph[root-1]:
        if child not in vis:
            dfs1(child)
    stack.append(root)

def dfs2(root):
    tvis.add(root)
    temp.append(root)
    for child in tgraph[root-1]:
        if child not in tvis:
            dfs2(child)


for x in range(1,nodes+1):
    if x not in vis:
        dfs1(x)

while stack:
    node=stack.pop()
    if node not in tvis:
        dfs2(node)
        ans.append(temp)
        temp=[]
    
print(ans)
    


        

