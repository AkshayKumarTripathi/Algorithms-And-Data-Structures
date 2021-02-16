class Tree:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

root=Tree(1)
a=Tree(3) 
b=Tree(3)
c=Tree(4)
d=Tree(-1)
e=Tree(-1)
f=Tree(4)

root.left=a
root.right=b
a.left=c
a.right=d
b.left=e
b.right=f

def mirror(L,R):
    if not L and not R:
        return True

    elif not L and R or L and not R:
        return False

    elif L.value==R.value:
        return mirror(L.left,R.right) and mirror(L.right , R.left)

    return False

def start(root=root):
    return mirror(root.left,root.right)

print(start())