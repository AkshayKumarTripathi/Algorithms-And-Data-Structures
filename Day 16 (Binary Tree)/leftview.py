# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.

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
root.right=b
b.left=e
b.right=f

start=[root]
def left(start=start):
    ans=[]
    while start:
        temp=[]
        for node in start:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        left=start[0]
        ans.append(left.value)
        start=temp

    return ans

print(left())

