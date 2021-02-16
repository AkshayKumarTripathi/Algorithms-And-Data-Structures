# Given a binary tree, 
# return the level order traversal of its nodes' values. (ie, from left to right, level by level).
class Tree:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

root=Tree(3)
a=Tree(9)
b=Tree(20)
c=Tree(15)
d=Tree(7)

root.left=a
root.right=b
b.left=c
b.right=d



ret=[]
holder=[root]
while holder!=[]:
    temp=[]
    replace=[]
    for x in holder:
        temp.append(x.value)
        if x.left:
            replace.append(x.left)
        if x.right:
            replace.append(x.right)
    ret.append(temp)
    holder=replace

print(ret)

    

    

