class Tree:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

root=Tree()
a=Tree(1)
b=Tree(2)
c=Tree(3)
d=Tree(4)
e=Tree(5)
f=Tree(6)
root.left=a
a.left=c
root.right=b
b.right=d
d.right=f
d.left=e

record=dict()
def top(root=root,x=0):
    if x in record.keys():
        pass
    else:
        record[x]=root.value

    if root.left:
        top(root.left,x-1)
    if root.right:
        top(root.right,x+1)
top()
print(record)
res=[]
minimum=min(record)
maximum=max(record)
for x in range(minimum,maximum+1):
    if x in record.keys():
        res.append(record[x])

print(res)