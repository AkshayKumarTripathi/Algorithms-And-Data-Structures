

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


root=Node(9)
four=Node(4)
one=Node(1)
eight=Node(8)
seven=Node(7)
five=Node(5)
six=Node(6)
fifteen=Node(15)
ten=Node(10)
twenty=Node(20) 
root.left=four
four.left=one
four.right=eight
eight.left=seven
seven.left=five
five.right=six
root.right=fifteen
fifteen.left=ten
fifteen.right=twenty

search=float(input('Enter the number you want to search on: '))

def ceil(root=root):
    if not root:
        return -1

    if root.val==search:
        return search
    
    if root.val>search:
        temp=ceil(root.left)
        return temp if temp>=search else root.val

    if root.val<search:
        return ceil(root.right)

    


def floor(root=root):
    if not root:
        return search+1

    if root.val==search:
        return search

    if root.val>search:
        return floor(root.left)
    
    if root.val<search:
        temp=floor(root.right)
        return temp if temp<=search else root.val
print(ceil(),floor())
