# Merge two sorted linked lists and return it as a new sorted list.
#  The new list should be made by splicing together the nodes of the first two lists.

class Linkedlist:
    def __init__(self,head):
        self.head=head
    
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

c1=Node(3)
b1=Node(2,c1)
a1=Node(1,b1)

c2=Node(6)
b2=Node(5,c2)
a2=Node(4,b2)

l1=Linkedlist(a1)
l2=Linkedlist(a2)

head1=l1.head
head2=l2.head


new=Node(None)
final=Linkedlist(new)
ret=final.head
while head1!= None and head2!=None:
    val1=head1.val
    val2=head2.val
    if val1<val2:
        temp=Node(val1)
        new.next=temp
        new=new.next
        head1=head1.next
    else:
        temp=Node(val2)
        new.next=temp
        new=new.next
        head2=head2.next

if head1!=None:
    new.next=head1
if head2!=None:
    new.next=head2


ret=ret.next
while ret!=None:
    print(ret.val)
    ret=ret.next


# Leet code constant space code (Practice)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if not l1 and not l2:
#             return l1
#         elif not l1:
#             return l2
#         elif not l2:
#             return l1
        
#         start = l1 if l1.val <= l2.val else l2
#         fix = l2 if start == l1 else l1
        
#         prev = start
#         runner = prev.next
#         while runner and fix:
#             while runner and runner.val < fix.val:
#                 prev = runner 
#                 runner = runner.next
#             prev.next = fix
#             fix = runner
#             prev = prev.next
#             runner = prev.next
        
#         if fix and prev:
#             prev.next = fix
        
#         return start