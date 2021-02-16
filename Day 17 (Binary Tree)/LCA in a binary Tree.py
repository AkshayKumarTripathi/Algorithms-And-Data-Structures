# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q 
# as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”



class Tree:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

root=Tree(1)
a=Tree(3) 
b=Tree(-10)
c=Tree(70)
d=Tree(-50)
e=Tree(2)




