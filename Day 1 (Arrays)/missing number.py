# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# We know that the sum of first n integers is n*(n+1)//2 so if we are given an array to find the missing number we can subtract the sum of 
# the array with the total sum of first n integers.
#

nums=[9,6,4,2,3,5,7,0,1]
total=sumation(nums)
length=len(nums)
length=length*(length+1)//2
print(length-total)