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

# with recursion
def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.value)
        inorder(root.right)



# without recursion
def inorder(root):
    current=root
    stack=[]
    while True:
        if current==None and stack==[]:
            break
        elif current==None and stack!=[]:
            temp=stack.pop()
            print(temp.value)
            current=temp.right

        else:
            stack.append(current)
            current=current.left


inorder(root)


        

