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
graph.add(1,3)
graph.add(3,4)
graph.add(3,5)
graph.add(5,6)
graph.add(2,7)
graph.add(7,8)
graph.add(7,9)


# print(graph.dfs(1))
        

distance=[-1]*9
vis=set()
extend=[6]
dis=0
while extend:
    temp=[]
    for x in extend:
        distance[x-1]=dis
        vis.add(x)
    dis+=1
    for x in extend:
        for child in graph.body[x]:
            if child not in vis:
                temp.append(child)

    extend=temp

print(distance)
    
        

    



                


