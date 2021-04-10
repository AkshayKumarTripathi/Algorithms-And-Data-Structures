# You are given an integer array nums sorted in ascending order, and an integer target.

# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# If target is found in the array return its index, otherwise, return -1.


nums=[3,1]
def array(nums,n,index=0):
    length=len(nums)
    if length==1:
        return nums,index

    else:
        middle=length//2
        if nums[0] <= n <= nums[middle-1]:
            return nums[0:middle],index
        if nums[middle]<=n<=nums[length-1]:
            return nums[middle:],index+middle

        if nums[0]<=nums[middle-1] and not nums[0]<=n<=nums[middle-1]:
            return array(nums[middle:],n,index+middle)

        else:   return array(nums[:middle],n,index)
               
n=3
nums,index=array(nums,n,index=0)
def search(nums,n,index):
    length=len(nums)
    middle=length//2
    if length==0 :
        return -1
    if nums[middle]==n:
        return middle+index
    else:
        if nums[middle]>n:
            return search(nums[:middle],n,index)
        else:   return search(nums[middle+1:],n,index+middle+1)

print(search(nums,n,index))