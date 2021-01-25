# Stack is a linear data structure which follows a particular order in which the operations are performed.
# The order may be LIFO(Last In First Out) or FILO(First In Last Out).

# Mainly the following three basic operations are performed in the stack:

# Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
# Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. 
# If the stack is empty, then it is said to be an Underflow condition.
# Peek or Top: Returns top element of stack.
# isEmpty: Returns true if stack is empty, else false.

class Stack:
    def __init__(self):
        self.body=[]
        self.size=0

    def push(self,value):
        self.body.append(value)
        self.size+=1
    
    def pop(self):
        self.size-=1
        return self.body.pop()
    
    def peek(self):
        if self.size>=1:
            return self.body[self.size-1]
        else:
            return None

    def isempty(self):
        if self.size<1:
            print('Yes The stack is empty')
        else:   print('The stack is not empty')

        

# Operations on Queue:
# Mainly the following four basic operations are performed on queue:

# Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.
# Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. 
# If the queue is empty, then it is said to be an Underflow condition.
# Front: Get the front item from queue.
# Rear: Get the last item from queue.

class Queue:
    def __init__(self):
        self.body=[]
        self.size=0

    def enqueue(self,value):
        self.size+=1
        self.body.insert(0,value)
    
    def dequeue(self,value):
        if self.size>=1:
            self.size-=1
            self.body.pop()

    def isempty(self):
        if self.size==0:
            return True
        return False

    def front(self):
        if self.size>=1:
            return self.body[self.size-1]

    def rear(self):
        if self.size>=1:
            return self.body[0]
    
    