# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


nums=[1,2,3]


def permutations(nums,length,start=0):
    if start==length:
        print(nums)

    else:
        for x in range(start,length):
            nums[start],nums[x]=nums[x],nums[start]
            start+=1
            permutations(nums,length,start)
            start-=1
            nums[start],nums[x]=nums[x],nums[start]

permutations(nums,len(nums))