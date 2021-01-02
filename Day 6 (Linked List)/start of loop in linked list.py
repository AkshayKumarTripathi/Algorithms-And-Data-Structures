# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Notice that you should not modify the linked list.

class Linkedlist:
    def __init__(self,head):
        self.head=head
    
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

h2=Node(1)
g2=Node(2,h2)
f2=Node(3,g2)
e2=Node(69,f2)
d2=Node(4,e2)
c2=Node(3,d2)
b2=Node(2,c2)
a2=Node(1,b2)

h2.next=e2

# Here we are going to use rabbit and hare approach.

rabbit=toro=a2

while rabbit!=None and rabbit.next!=None:
    rabbit=rabbit.next.next
    toro=toro.next
    if rabbit==toro:
        break

rabbit=a2
while rabbit!=toro:
    rabbit=rabbit.next
    toro=toro.next

print(rabbit.val)
