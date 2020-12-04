# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.


array=[2,2,1,1,1,2,2]

# We are going to use Moore's-Voting algorithm. O(N) Time complexity and O(1) space

majority_ele=0
count=0
for x in array:
    if count==0:
        majority_ele=x
    if majority_ele==x:
        count+=1
    else:   count-=1

print(majority_ele)


# less space optimized approach O(N) Time and O(N) space
# record={}
# look=len(array)//2

# for x in array:
#     if x in record.keys():
#         record[x]+=1
#         if record[x]>look:
#             print(x)
#             break
#     else:
#         record[x]=1

