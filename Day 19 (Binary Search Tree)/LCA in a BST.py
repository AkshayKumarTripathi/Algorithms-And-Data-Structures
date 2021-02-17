# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q 
# as descendants (where we allow a node to be a descendant of itself).”


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


root=Node(6)
two=Node(2)
eight=Node(8)
seven=Node(7)
nine=Node(9)
zero=Node(0)
four=Node(4)
three=Node(3)
five=Node(5)

root.left=two
root.right=eight
eight.left=seven
eight.right=nine
two.left=zero
two.right=four
four.left=three
four.right=five



big=9
small=0

def find(root=root):
    if root:
        val=root.val
        if val==big or val==small:
            return root
        elif small<val<big:
            return root
        elif val>big:
            return find(root.left)
        else:
            return find(root.right)
        
    return None

print(find().val)