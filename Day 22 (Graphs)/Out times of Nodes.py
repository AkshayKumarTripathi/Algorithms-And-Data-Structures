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
graph.add(4,5)
graph.add(5,6)
graph.add(6,7)
graph.add(4,8)
graph.add(7,8)




dis=[-1]*8
out=[-1]*8
time=0
vis=set()
def inout(node=1):
    global time
    vis.add(node)
    dis[node-1]=time
    time+=1
    for child in graph.body[node]:
        if child not in vis:
            inout(child)

    out[node-1]=time
    time+=1


inout()
print(dis)

print()

print(out)
    
    