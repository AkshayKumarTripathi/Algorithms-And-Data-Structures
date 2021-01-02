class Linkedlist:
    def __init__(self,head):
        self.head=head
    
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next



g2=Node(9)
f2=Node(9,g2)
e2=Node(9,f2)
d2=Node(9,e2)
c2=Node(9,d2)
b2=Node(1,c2)
a2=Node(4,b2)
g2.next=a2
fast=slow=a2
while  fast!=None and fast.next!=None :
    fast=fast.next.next
    slow=slow.next
    if fast==slow:
        
        print('yes a link is present')
        break
    
