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


new=linked.head

new=new.next
new.val=new.next.val
new.next=new.next.next