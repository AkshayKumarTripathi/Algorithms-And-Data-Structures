# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# Follow up: Could you implement the O(n) solution? 

# The naive aproach will be to sort the array and then traverse the array to see the largest subarray O(Nlog(N))(to sort the array) and O(N)
# (To check the largest array)

# nums.sort()
# print(nums)
# count=0
# temp=0
# for x in range(len(nums)-1):
#     if nums[x]+1==nums[x+1]:
#         temp+=1
#     if temp>count:
#         count=temp
# print(count+1)
    
nums = [102,101,1,2,4,3,5,6]
record={}
count=0
for x in nums:
    record[x]=1

for x in nums:
    if x-1 not in record.keys():
        temp=0
        while x in record.keys():
            x+=1
            temp+=1
        if temp>count:
            count=temp
print(count)

    




