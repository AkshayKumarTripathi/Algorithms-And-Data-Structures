# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

# You need to return the number of important reverse pairs in the given array.



array=[40,25,19,12,9,6,2]

def reverse(nums):
    length=len(nums)
    # Base Case
    if length<=1:
        return nums,0

    else:
        middle=length//2
        left,rev_left=reverse(nums[:middle])
        right,rev_right=reverse(nums[middle:])

        new=[]
        count=0
        i=j=0
        len_left=len(left)
        len_right=len(right)

        while i<len_left and j<len_right:
        #  Condition is i<j and a[i]>2*a[j]
            if left[i]>right[j]*2:
                j+=1
                count+=(len_left-i)
            else:   i+=1

        i=j=0

        while i<len_left and j<len_right:
            a,b=left[i],right[j]
            if a<b:
                new.append(a)
                i+=1
            else:
                new.append(b)
                j+=1

        if j!=len_right:
            new+=right[j:]
        elif i!=len_left:
            new+=left[i:]
            
        return new,count+rev_left+rev_right
    
print(reverse(array)[1])

# Brute Force Approach O(N**2) Time complexity.

# for x in range(len(array)-1):
#     for y in range(x,len(array)):
#         if array[x]>2*array[y]:
#             count+=1
# print(count)
















