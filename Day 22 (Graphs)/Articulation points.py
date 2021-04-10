class Graph:
    def __init__(self):
        self.body={}

    def add(self , first: int , second: int) -> None:
        if first in self.body.keys():
            if second not in self.body[first]:
                self.body[first].append(second)
            
        else:   self.body[first]=[second]

        if second in self.body.keys():
            if first not in self.body[second]:
                self.body[second].append(first)

        else:   self.body[second]=[first]
    
    

        

graph=Graph()

graph.add(1,2)
graph.add(2,3)
graph.add(3,4)
graph.add(4,2)
graph.add(1,7)
graph.add(7,6)
graph.add(6,1)
graph.add(1,5)
graph.add(5,8)
graph.add(8,9)
graph.add(9,5)
graph.add(5,10)
graph.add(10,11)
graph.add(10,12)
graph.add(12,13)
graph.add(12,5)

dis=[-1]*15
low=[-1]*15

vis=set()
time=0
total=0

def dfs(child,parent=-1):
    global time,total
    vis.add(child)
    dis[child-1]=time
    low[child-1]=time
    time+=1
    children=0
    for connect in graph.body[child]:
        if connect==parent:
            continue

        if connect in vis:
            low[child-1]=min(low[child-1],dis[connect-1])
        
        else:
            dfs(connect,child)
            low[child-1]=min(low[child-1], low[connect-1])
            if low[connect-1]>=dis[child-1] and parent!=-1:
                print(child)
                total+=1
            children+=1
    if parent==-1 and children>1:
        print(child)
        total+=1

dfs(1)
print()
print()
print(total)
