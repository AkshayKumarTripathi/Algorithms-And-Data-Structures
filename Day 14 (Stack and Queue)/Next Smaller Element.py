# Given an array, print the Next Smaller Element (NSE) for every element. 
# The Smaller smaller Element for an element x is the first smaller element on the right side of x in array. 
# Elements for which no smaller element exist (on right side), consider next smaller element as -1.

# Examples:
# a) For any array, rightmost element always has next smaller element as -1.
# b) For an array which is sorted in increasing order, all elements have next smaller element as -1.
# c) For the input array [4, 8, 5, 2, 25}, the next smaller elements for each element are as follows.

# Element       NSE
#    4      -->   2
#    8      -->   5
#    5      -->   2
#    2      -->   -1
#    25     -->   -1

# I am going to use dictonary and a stack to create a map

nums1=[2,1,0,3,7,4]
nums2=[2,1,3,4,5,7,9,0]

result=[]
stack=[]
record={}

for x in nums2:
    while len(stack)>=1 and stack[-1]>x:
        record[stack.pop()]=x
    stack.append(x)

for x in nums1:
    temp=record.get(x,-1)
    result.append(temp)

print(result)
