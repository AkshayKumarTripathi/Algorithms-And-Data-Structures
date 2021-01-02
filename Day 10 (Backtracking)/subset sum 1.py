# Given a non-empty array nums containing only positive integers,
#  find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

nums=[1,5,11,5]
total=sum(nums)
a=[False]

# This code is slow
def part(total,nums,curr=0,start=0,length=len(nums),half=total//2):
    if total==curr:
        a[0]=True
        return None

    else:
        for x in range(start,length):
            num=nums[x]
            if total-num<half:
                continue
            else:
                total-=num
                curr+=num
                start+=1
                part(total,nums,curr,start)
                if a[0]==True:
                    break
                total+=num
                curr-=num

        return None
part(total,nums,curr=0,start=0,length=len(nums),half=total//2)
print(a[0])