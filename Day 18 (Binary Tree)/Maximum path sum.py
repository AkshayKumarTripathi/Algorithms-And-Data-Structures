

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
ans=0
def maxi(root=root):
    if not root:
        return 0

    current=root.value
    left=max(maxi(root.left),0)
    right=max(maxi(root.right),0)
    global ans
    ans=max(ans,left+right+current)
    return current+max(left,right)

maxi()
print(ans)



