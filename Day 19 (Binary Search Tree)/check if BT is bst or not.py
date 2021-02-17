# We will use the BST property that INORDER traversal of BST is sorted

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


def is_BST(root=root):
    if root:
        stack=[]
        while root:
            stack.append(root)
            root=root.left
        value=stack[-1].val-1
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            if root.val<=value:
                return False
            value=root.val
            root=root.right
    return True

print(is_BST())