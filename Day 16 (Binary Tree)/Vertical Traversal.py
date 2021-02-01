class Tree:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

root=Tree(1)
a=Tree(2)
b=Tree(3)
c=Tree(4)
d=Tree(5)
e=Tree(6)
f=Tree(7)
root.left=a
root.right=b
a.left=c
a.right=d
b.left=e
b.right=f

record={}


def vertical(record=record,root=root,x=0,y=0):
    if root:
        if y in record.keys():
            if x in record[y].keys():
                record[y][x].append(root.value)
            else:
                record[y][x]=[]
                record[y][x].append(root.value)
        else:
            record[y]=dict()
            record[y][x]=[]
            record[y][x].append(root.value)
        vertical(record,root.left,x+1,y-1)
        vertical(record,root.right,x+1,y+1)

    return

vertical()
minimum=min(record)
maximum=max(record)
ret=[]
for x in range(minimum,maximum+1):
    if x in record.keys():
        temp_min=min(record[x])
        temp_max=max(record[x])
        temp=[]
        for y in range(temp_min,temp_max+1):
            if y in record[x].keys():
                temp+=list(sorted(record[x][y]))
        ret.append(temp)
print(ret)



        
