

nums=[1,1,1,2,2,3,3,4,4,4]
nums.sort()
out=[]
target=9
length=len(nums)
prev_a=prev_b=nums[0]-1
for a in range(length):
    if nums[a]==prev_a:
        continue
    else:
        prev_a=nums[a]
        for b in range(a+1,length):
            if nums[b]==prev_b:
                continue
            else:
                prev_b=nums[b]
                wanted=target-nums[a]-nums[b]
                left=b+1
                right=length-1
                while left<right:
                    if nums[left]+nums[right]==wanted:
                        out.append([nums[a],nums[b],nums[left],nums[right]])
                        left+=1
                        right-=1
                    if nums[left]+nums[right]>wanted:
                        temp=nums[right]
                        right-=1
                        while nums[right]==temp:
                            right-=1
                    if nums[left]+nums[right]<wanted:
                        temp=nums[left]
                        left+=1
                        while nums[left+1]==nums[left]:
                            left+=1
print(out)

