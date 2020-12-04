# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
nums=[3,2,3]

num_1=num_2=0
c_1=c_2=0
times=len(nums)//3
ret=[]
for x in nums:
    if c_1==0 and x!=num_2:
        num_1=x
    elif c_2==0 and x!=num_1:
        num_2=x
    if num_1==x:
        c_1+=1
    elif num_2==x:
        c_2+=1
    else:
        c_1-=1
        c_2-=1
c_1=c_2=0
for x in nums:
    if x==num_1:
        c_1+=1
    if x==num_2:
        c_2+=1
if c_1>times:
    ret.append(num_1)
if c_2>times:
    if num_2 not in ret:
        ret.append(num_2)
print(ret)




    
    
    