# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

nums=[2,3,1,3,3]

i=len(nums)-1
did=False
for x in range(i,0,-1):
    if nums[x-1]<nums[x]:
        did=True
        border=x-1
        changer=-1
        changer_index=-1
        for index,new in enumerate(nums[x:]):
            if changer==-1:
                changer=new
                changer_index=border+index+1
            elif new>nums[border] and new<=changer:
                changer=new
                changer_index=border+index+1
        nums[border],nums[changer_index]=nums[changer_index],nums[border]
        nums=nums[:border+1]+nums[border+1:][::-1]
        print(nums)
        break

if not did:
    nums=nums[::-1]
    print(nums)

            