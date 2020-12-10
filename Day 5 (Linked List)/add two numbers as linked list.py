# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


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
b2=Node(9,c2)
a2=Node(9,b2)

e1=Node(9)
c1=Node(9,e1)
b1=Node(9,c1)
a1=Node(9,b1)

l1=Linkedlist(a1)
l2=Linkedlist(a2)

head1=ret=l1.head
head2=l2.head

carry=0
while head1.next!=None and head2.next!=None:
    addition  = head1.val+head2.val + carry
    head1.val = addition%10 
    carry = addition//10
    head1=head1.next
    head2=head2.next

if head1.next==None:
    addition  = head1.val+head2.val + carry
    head1.val = addition%10 
    carry = addition//10
    head2=head2.next
    while head2!=None:
        addition=head2.val+carry
        temp=Node(addition%10)
        head1.next=temp
        head1=head1.next
        carry=addition//10
        head2=head2.next

    if carry!=0:
        temp=Node(carry)
        head1.next=temp

else:
    addition=head1.val+head2.val+carry
    head1.val=addition%10
    carry=addition//10
    head1=head1.next
    while head1.next!=None:
        addition=head1.val+carry
        head1.val=addition%10
        carry=addition//10
        head1=head1.next

    addition=head1.val+carry
    head1.val=addition%10
    if addition>=10:
        temp=Node(carry)
        head1.next=temp

while ret!=None:
    print(ret.val)
    ret=ret.next


# better looking solution from leet code

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = ListNode()
#         cur = dummy
        
#         carry = 0
#         while l1 or l2 or carry:
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0
            
#             # compute digit
#             val = v1 + v2 + carry
#             carry = val // 10
#             val %= 10
#             cur.next = ListNode(val)
            
#             # update pointers
#             cur = cur.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
        
#         return dummy.next