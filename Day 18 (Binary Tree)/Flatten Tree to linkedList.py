# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the
# list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.



class Tree:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

        
root=Tree(-1)
a=Tree(3) 
b=Tree(-10)
c=Tree(-70)
d=Tree(-50)
e=Tree(2)

root.left=a
root.right=b
a.left=c
a.right=d
b.left=e



stack=[]
def create(root=root):
    if root:

        stack.append(root)
        create(root.left)
        create(root.right)
        root.left=None
        root.right=None
    return None
create()
for x in range(1,len(stack)):
    stack[x-1].right=stack[x]
root=stack[0]