# Create a BST

class Node:
    def __init__(self,val,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Tree:
    def __init__(self):
        self.head=None

    def find(self,node,value):
        if node.val>value:
            if not node.left:
                return node
            return self.find(node.left,value)
        elif node.val<value:
            if not node.right:
                return node
            return self.find(node.right,value)
        return None
 
    def add(self,value):
        if self.head:
            where=self.find(self.head,value)
            if where and value>where.val:
                temp=Node(value)
                where.right=temp
            elif where and value<where.val:
                temp=Node(value)
                where.left=temp
                
        else:
            self.head=Node(value)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val,end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=' ')

BST=Tree()

nums=[6,2,8,0,4,7,9,3,5]
for x in nums:
    BST.add(x)

preorder(BST.head)

    
    