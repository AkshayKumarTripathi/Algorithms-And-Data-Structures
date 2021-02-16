# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]


class Tree:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

i=-1
def create(inorder):
    if inorder==[]: 
        return None
    else:
        global i
        i+=1
        value=preorder[i]
        head=Tree(value)
        length=len(inorder)
        temp=0
        while temp<length and inorder[temp]!=value:
            temp+=1
        left=inorder[:temp]
        right=inorder[temp+1:]
        L=create(left)
        R=create(right)
        head.left=L
        head.right=R
        return head
    
ans=create(inorder)

def inord(ans=ans):   # For verifiacation
    if ans:
        inord(ans.left)
        print(ans.value,end=' ')
        inord(ans.right)

inord()