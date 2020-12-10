# Reverse a singly linked list.

class Linkedlist:
    def __init__(self,head):
        self.head=head
    
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

        
d=Node(4)
c=Node(3,d)
b=Node(2,c)
a=Node(1,b)
Linked=Linkedlist(a)

prev=None
temp=Linked.head
current=Linked.head
after=current.next

while temp!=None:
    print(temp.val)
    temp=temp.next

print()

while current!=None:
    current.next=prev
    prev=current
    current=after
    if current==None:
        break
    after=current.next

while prev!=None:
    print(prev.val)
    prev=prev.next


# recursion based
# def reverse(prev,current,after):
#     if current==None:
#         return prev
#     else:
#         current.next=prev
#         prev=current
#         current=after
#         if current!=None:
#             after=after.next
#         return reverse(prev,current,after)

# temp=reverse(prev,current,after)
# while temp!=None:
#     print(temp.val)
#     temp=temp.next