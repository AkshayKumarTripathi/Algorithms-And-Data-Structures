# Given a singly linked list, determine if it is a palindrome.


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
e2=Node(4,f2)
d2=Node(4,e2)
c2=Node(3,d2)
b2=Node(2,c2)
a2=Node(1,b2)

record=[]
length=-1
while a2!=None:
    record.append(str(a2.val))
    a2=a2.next
    length+=1

start=0
while start<=length:
    if record[start]==record[length]:
        start+=1
        length-=1

    else:
        print('Not Palindrome')
        break

