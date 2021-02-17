# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
# If such a node does not exist, return null.

# WE WILL USE THE BST PROPERTY TO FIND THE APPROPRIATE NODE

def find(root,value):
    if root:
        if root.value==value:
            return root

        elif root.value>value:
            return find(root.left,value)
        
        else:
            return find(root.right,value)
    return None