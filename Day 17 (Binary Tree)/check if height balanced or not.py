# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



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

ans=True
def check(root=root):
    if not root:
        return 0

    else:
        left=check(root.left)
        right=check(root.right)
        if abs(left-right)>1:
            global ans
            ans=False
        return max(left,right)+1

check()
print(ans)
        


