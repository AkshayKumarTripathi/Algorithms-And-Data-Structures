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

    def dfs(self , node : int) -> list:
        check=set()
        stack=[node]
        ret=[]        
        while stack:
            temp=stack.pop()
            if temp not in check:
                ret.append(temp)
                check.add(temp)
                stack+=self.body[temp]

        return ret
    
    

        

graph=Graph()

graph.add(1,2)
graph.add(1,7)
graph.add(1,3)
graph.add(3,4)
graph.add(3,5)
graph.add(5,6)
graph.add(5,7)
graph.add(6,8)
graph.add(6,4)
graph.add(4,2)
graph.add(2,8)
graph.add(7,8)







nodes=[-10]*100
vis=set()
def bipart(root=1,col=1):
    vis.add(root)
    nodes[root-1]=col
    for x in graph.body[root]:
        if x not in vis:
            if bipart(x,col^1)==False:
                return False
        if nodes[root-1]==nodes[x-1]:
            return False

    return True
    

print(bipart())
