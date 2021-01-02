# Find the maximum numbers of one

nums=[1,1,1,1,1,1,1,1,1,1,1]
ans=0
temp=0
for x in nums:
    if x==1:
        temp+=1

    else:
        ans=temp if temp> ans else ans
        temp=0

print(max(temp,ans))
