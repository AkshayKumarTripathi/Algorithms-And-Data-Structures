nums=[1,2,2,2,3,3,3,4,5,5,6]
i=1
till=1
for x in range(1,len(nums)):
    if nums[x]!=nums[x-1]:
        nums[i]=nums[x]
        i+=1
        till+=1

print(nums[:till])
