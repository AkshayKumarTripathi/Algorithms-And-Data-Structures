class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


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

record={}
addition=int(input('Enter the sum for pair: '))
def find(root=root):
    if root:
        if root.val in record.keys():
            return root.val

        record[addition-root.val]=root
        return find(root.left) or find(root.right)

print(find())