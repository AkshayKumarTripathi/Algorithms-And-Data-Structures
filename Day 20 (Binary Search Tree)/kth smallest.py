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


smallest=int(input('Enter the kth smallest number you want to find: '))

stack=[]
while root:
    stack.append(root)
    root=root.left

i=0
while stack or root:
    while root:
        stack.append(root)
        root=root.left

    root=stack.pop()
    i+=1
    if i==smallest:
        print(root.val)
        break
    root=root.right




