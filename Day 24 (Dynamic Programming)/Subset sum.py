nums=[1,1,1]
# find=11
total=sum(nums)
if total%2==1:
    print(False)
total//=2
length=len(nums)
table=[[None for _ in range(total+1)] for _ in range(length+1)]
def ans(length=length,find=total):
    if table[length][find]!=None:
        return table[length][find]
    
    if find==0:
        return True

    if length==0:
        if find==0:
            return True
        return False

    num=nums[length-1]

    if find-num>=0:
        temp= ans(length-1, find-num) or ans(length-1 , find)
        table[length][find]=temp
        return temp
       
    temp= ans(length-1 , find)
    table[length][find]=temp
    return temp


print(ans())
    
        



        




