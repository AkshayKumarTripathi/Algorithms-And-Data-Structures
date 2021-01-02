# Find three numbers in an array such that a + b + c = 0
#v we are going to use 2 pointer method   

nums=[-4,-1,-1,0,1,1,2,2]
ans=[]
for x in range(len(nums)-2):
    if x==0 or nums[x]!=nums[x-1]:
        low=x+1
        high=len(nums)-1
        req=0-nums[x]
        if req<0:
            break   # Since the array is sorted once we encounter the case where the required becomes more than 0 it is impossible to find 
                    # the other two numbers in the positive side 
        while low<high:
            if nums[low]+nums[high]==req:
                ans.append([nums[x],nums[low],nums[high]])

                left_val=nums[low]
                low+=1
                while low<len(nums) and left_val==nums[low]:
                    low+=1
                
                right_val=nums[high]
                high-=1
                while high>x and nums[high]==right_val:
                    high-=1

            elif nums[low]+nums[high]<req:
                left_val=nums[low]
                low+=1
                while low<len(nums) and left_val==nums[low]:
                    low+=1

            else:
                right_val=nums[high]
                high-=1
                while high>x and nums[high]==right_val:
                    high-=1


print(ans)



