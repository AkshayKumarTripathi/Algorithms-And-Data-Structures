# Given the head of a linked list, rotate the list to the right by k places.

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

k=int(input('Enter the rotation number here: '))

temp=a2
length=0
while temp!=None:
    temp=temp.next
    length+=1

k=k%length

fast=slow=a2
for _ in range(k):
    fast=fast.next

while fast.next!=None:
    fast=fast.next

    slow=slow.next

temp=slow.next
slow.next=None
fast.next=a2
while temp!=None:
    print(temp.val)
    temp=temp.next
    
