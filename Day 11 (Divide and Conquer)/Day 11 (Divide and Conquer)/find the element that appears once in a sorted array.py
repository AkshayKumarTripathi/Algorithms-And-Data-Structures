# You are given a sorted array consisting of only integers where every element appears exactly twice,
#  except for one element which appears exactly once. Find this single element that appears only once.

# Follow up: Your solution should run in O(log n) time and O(1) space

#                                           see the leet code most voted solution as well

nums=[1,3,3,4,4,8,8,9,9]
def single(nums):
    if len(nums)==1:
        return nums[0]
    if len(nums)==3:
        middle=1
        if nums[middle]==nums[middle-1]:
            return nums[middle+1]
        return nums[0]
    middle=len(nums)//2
    if nums[middle]!=nums[middle-1] and nums[middle]!=nums[middle+1]:
        return nums[middle]

    if middle%2==0:
        if nums[middle]==nums[middle+1]:
            return single(nums[middle+2:])
        
        return single(nums[:middle-1])
    elif middle%2!=0 :
        if nums[middle]==nums[middle-1]:
            return single(nums[middle+1:])
        return single(nums[:middle])


print(single(nums))