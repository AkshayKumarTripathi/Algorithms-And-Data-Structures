nodes=4
graph=[[0,1],[1,2],[2,0],[1,3]]
g={}
for x in graph:
    if x[0] in g.keys():
        g[x[0]].append(x[1])
    else:   g[x[0]]=[x[1]]

    if x[1] in g.keys():
        g[x[1]].append(x[0])
    
    else:   g[x[1]]=[x[0]]

graph=g

time=1

dis=[-1]*nodes
low=[-1]*nodes
ret=[]
vis=set()

def dfs(child,parent=-1):
    global time
    low[child]=time
    dis[child]=time
    time+=1
    vis.add(child)
    for connect in graph[child]:
        if connect==parent or connect==child:
            continue
        if connect in vis:
            low[child]=min(low[child],dis[connect])
        else:
            dfs(connect,child)
            low[child]=min(low[child],low[connect])
            if low[connect]>dis[child]:
                ret.append([connect,child])
                
for i in range(nodes):
    if i not in vis:
        dfs(i)
        
print(ret)
