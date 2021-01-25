# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
# If it does not exist, output -1 for this number.

nums1 = [4,1,2,3]
nums2 = [1,3,4,2]

stack=[]
result=[]
record={}
for x in nums2:
    while len(stack)>=1 and stack[-1]<x:
        record[stack.pop()]=x
    stack.append(x)

for x in nums1:
    if x in record.keys():
        result.append(record[x])
    else:   result.append(-1)

print(result)
