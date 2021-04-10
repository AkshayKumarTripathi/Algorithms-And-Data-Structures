nums=[2,3,5,6,8,10]
target=10
length=len(nums)
table=[[-1 for _ in range(target+1)] for _ in range(length+1)]

def ans(length=length,target=target):
    if table[length][target]!=-1:
        return table[length][target]
    if target==0:
        return 1
    if length==0:
        return 0
    num=nums[length-1]
    if target-num>=0:
        temp = ans(length-1,target-num) + ans(length-1,target)
        table[length][target]=temp
        return temp
    temp=ans(length-1,target)
    table[length][target]=temp
    return temp

print(ans())
