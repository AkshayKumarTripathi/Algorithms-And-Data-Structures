# Implementing Graph
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
graph.add(7,4)
graph.add(4,1)
graph.add(1,2)
graph.add(1,3)
graph.add(7,3) #
graph.add(2,5)
graph.add(3,6)


vis=set()
def cycle(node=1, parent=-1):
    vis.add(node)
    for child in graph.body[node]:
        if child==parent:
            continue
        elif child in vis:
            return True

        else:
            if cycle(child,node)==True:
                return True


    return False


print(cycle())