# Find the power set of a list of numbers

nums=[1,2,3]
length=len(nums)
ret=[]
size=2**length
for n in range(size):
    ret.append([nums[i] for i in range(length) if (1<<i & n)!=0])
print(ret)


