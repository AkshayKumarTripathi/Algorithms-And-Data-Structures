class Node:
    def __init__(self,val,next=None,random=None):
        self.val=val
        self.next=next
        self.random=random


# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.

# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node

one=Node(7)
two=Node(13)
three=Node(11)
four=Node(10)
five=Node(1)
one.next=two
two.next=three
three.next=four
four.next=five
one.random=None
two.random=one
three.random=five
four.random=three
five.random=one

traverse=one
while traverse!=None:
    clone_temp=Node(traverse.val)
    future=traverse.next
    traverse.next=clone_temp
    clone_temp.next=future
    traverse=future
    
traverse=one
temp=traverse.next
while traverse!=None:
    temp.random= None if traverse.random==None else traverse.random.next
    traverse=traverse.next.next
    if temp.next!=None:
        temp=temp.next.next
        

ret=temp=one.next
while temp!=None:
    temp.next=None if temp.next==None else temp.next.next
    temp=temp.next

while ret!=None:
    print(ret.val,ret.random.val if ret.random!=None else ' NONE ')
    ret=ret.next

