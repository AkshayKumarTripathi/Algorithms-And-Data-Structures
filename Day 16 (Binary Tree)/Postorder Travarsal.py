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


def postorder(root):
    stack=[]
    i=1
    while True:
        while root :
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root=root.left
        root=stack.pop()
        if root.right!=None  and len(stack)>=1 and stack[-1]==root.right:
            stack.pop()
            stack.append(root)
            root=root.right
        else:
            print(root.value)
            root=None
        if len(stack)==0:
            break
        



postorder(root)

