# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
# find the area of largest rectangle in the histogram.

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

# The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

# Example:

# Input: [2,1,5,6,2,3]
# Output: 10 (5X2)
 
nums=[1,1]
res=[]
stack=[]
i=temp=len(nums)
for x in nums[::-1]:
    while len(stack)>=1 and stack[-1][0]>=x:
        stack.pop()
    if stack==[]:
        res.append(temp)
    else:
        res.append(stack[-1][1])
    i-=1
    stack.append([x,i])

res=res[::-1]
les=[]
stack=[]
i=temp=-1
for x in nums:
    while len(stack)>=1 and stack[-1][0]>=x:
        stack.pop()
    if len(stack)==0:
        les.append(temp)
    else:
        les.append(stack[-1][1])
    i+=1
    stack.append([x,i])
maxi=0
for x in range(len(nums)):
    temp=(res[x]-les[x]-1)*nums[x]
    maxi=max(temp,maxi)
print(les,res)
    