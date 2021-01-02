# Write a program to find the node at which the intersection of two singly linked lists begins.

# For example, the following two linked lists:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Each value on each linked list is in the range [1, 10^9].
# Your code should preferably run in O(n) time and use only O(1) memory./


class Linkedlist:
    def __init__(self,head):
        self.head=head
    
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

c=Node(5)
b=Node(4,c)
a=Node(8,b)

g2=Node(9,a)
f2=Node(9,g2)
e2=Node(9,f2)
d2=Node(9,e2)
c2=Node(9,d2)
b2=Node(1,a)
a2=Node(4,b2)

e1=Node(9,a)
c1=Node(1,a)
b1=Node(6,c1)
a1=Node(5,b1)


temp1=a1
temp2=a2
pp=None
for _ in range(2):
    while temp1.next!=None and temp2.next!=None:
        temp1=temp1.next
        temp2=temp2.next

    temp1=a2 if temp1.next==None else temp1.next
    temp2=a1 if temp2.next==None else temp2.next


while temp1!=None and temp2!=None:
    if temp1==temp2:
        pp=temp1.val
        break

    else:
        temp1=temp1.next
        temp2=temp2.next

print(pp)
