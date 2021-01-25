# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.


class min_stack:
    def __init__(self):
        self.body=[]

    def push(self,num):
        temp=self.getmin()
        if len(self.body)==0 or temp>num:
            self.body.append([num,num])
        else:
            self.body.append([num,temp])

    def getmin(self):
        return self.body[-1][1] if len(self.body)!=0 else -1
    
    def pop(self):
        self.body.pop()

    def peek(self):
        return self.body[-1][0]

