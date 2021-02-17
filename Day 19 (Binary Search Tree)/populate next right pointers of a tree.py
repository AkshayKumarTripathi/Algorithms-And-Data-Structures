


# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            body=[root]
            while body:
                length=len(body)
                body.append(None)
                for x in range(1,length):
                    body[x-1].next=body[x]

                body.pop()
                temp=[]
                for x in body:
                    if x.left==None:
                        break
                    temp.append(x.left)
                    temp.append(x.right)

                body=temp
            
        return root