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
graph.add(1,4)
graph.add(4,5)
graph.add(5,6)
graph.add(1,3)
graph.add(2,3)
graph.add(2,7)
graph.add(7,8)
graph.add(8,3)
graph.add(3,9)
graph.add(9,10)


far=0
vis=set()
start=-1
end=-1
distance=-1

extend=[1]
while extend:
    temp=[]
    for x in extend:
        vis.add(x)
        if far>distance:
            distance=far
            start=x

    far+=1

    for x in extend:
        for child in graph.body[x]:
            if child not in vis:
                temp.append(child)

    extend=temp



vis=set()

extend=[start]
distance=far=0
while extend:
    temp=[]
    for x in extend:
        vis.add(x)
        if far>distance:
            distance=far
            end=x

    far+=1

    for x in extend:
        for child in graph.body[x]:
            if child not in vis:
                temp.append(child)

    extend=temp


print(start,end)

print(distance) 
        
