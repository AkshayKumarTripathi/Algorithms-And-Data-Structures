
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



def preorder_(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)



# without recursion

def preorder(root) -> None :
    stack=[]
    while True:
        if stack==[] and root==None:
            break
        else:
            if root==None:
                temp=stack.pop()
                root=temp.right
            else:
                print(root.value)
                stack.append(root)
                root=root.left

preorder_(root)
print()
preorder(root)
