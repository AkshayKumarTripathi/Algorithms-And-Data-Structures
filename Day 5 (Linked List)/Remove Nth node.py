# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Follow up: Could you do this in one pass?


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

newa=Linked.head
remove=int(input('Enter the number here to remove: '))
fast=slow=newa
i=1
while i<=remove:
    i+=1
    fast=fast.next

if fast==None:
    newa=newa.next

    while newa!=None:
        print(newa.val)
        newa=newa.next

else:
    while fast!=None and fast.next!=None:
        fast=fast.next
        slow=slow.next
    
    slow.next=slow.next.next
    while newa!=None:
        print(newa.val)
        newa=newa.next