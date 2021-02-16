# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along 
# the longest path from the root node down to the farthest leaf node.




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
a.left=c
a.right=d
b.left=e
b.right=f

def height(root=root,high=0):
    if root:
        return max(height(root.left,high+1),height(root.right,high+1))
    return high

print(height())