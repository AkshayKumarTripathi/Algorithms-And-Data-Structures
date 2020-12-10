# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

class Linkedlist:
    def __init__(self,head):
        self.head=head
    
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

f=Node(6)
e=Node(5,f)     
d=Node(4,e)
c=Node(3,d)
b=Node(2,c)
a=Node(1,b)
Linked=Linkedlist(a)

# Basic approach will be to traverse the linked list and storing the length of LL now we will find the middle of LL and then will run a loop 
# again to return the middle element

#The optimized approach will be to use turtle and rabbit approach, which will solve it in a single pass.

turtle=rabbit=Linked.head

while rabbit!=None and rabbit.next!=None:
    rabbit=rabbit.next.next
    turtle=turtle.next

print(turtle.val)
