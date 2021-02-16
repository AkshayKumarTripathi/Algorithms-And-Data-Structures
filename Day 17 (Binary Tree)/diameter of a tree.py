# Given a binary tree, you need to compute the length of the diameter of the tree. 
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.

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
a.left=b
a.right=c
b.left=d
c.right=e

ans=1
def height(root=root):
    if not root:
        return 0

    else:
        L=height(root.left)
        R=height(root.right)
        global ans
        ans=max(ans,L+R+1)
        return max(L,R)+1

height()
print(ans-1)


