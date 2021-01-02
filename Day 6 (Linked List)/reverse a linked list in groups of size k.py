# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# Follow up:

# Could you solve the problem in O(1) extra memory space?
# You may not alter the values in the list's nodes, only nodes itself may be changed.


class Linkedlist:
    def __init__(self,head):
        self.head=head
    
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

h2=Node(8)
g2=Node(7,h2)
f2=Node(6,g2)
e2=Node(5,f2)
d2=Node(4,e2)
c2=Node(3,d2)
b2=Node(2,c2)
a2=Node(1,b2)

head=a2

length=0
while head!=None:
    length+=1
    head=head.next

k=int(input('Enter the number of pieces in which you want to divide the linked list : '))
times = length//k

# one loop will run times time
# the loop inside of that will do the reverse stuff

# dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> None
head=a2
ran_start=Node(None,head)
ret=None
ran_end=head
for _ in range(k):
    ran_end=ran_end.next

for _ in range(times):
    start=ran_start.next
    end=start
    for _ in range(k-1):
        end=end.next

    prev=None
    curr=start
    for _ in range(k):
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp

    ran_start.next=prev
    start.next=ran_end
    if ret==None:
        ret=ran_start

    i=0
    while i<k and ran_end!=None and ran_start!=None:
        ran_start=ran_start.next
        ran_end=ran_end.next
        i+=1

while ret!=None:
    print(ret.val)
    ret=ret.next
    










