# what we need to do
# Make a queue and see if the element we are adding is greater than the previous, if it is we can say for sure 
# for index in the range i,i+k the number we added will be maximum

queue=[]
nums=[1,3,1,2,0,5]
k=int(input('Enter the number here: ')) # all K are valid k will always will be smaller than len(nums)
for i in range(k):
    while len(queue)>=1 and queue[-1]<nums[i]:
        queue.pop()

    queue.append(nums[i])

ret=[]
ret.append(queue[0])
i=k 

while i<len(nums):
    removing=nums[i-k]
    if removing==queue[0]:
        queue.pop(0)
    while len(queue)>=1 and queue[-1]<nums[i]:
        queue.pop()
    queue.append(nums[i]) 
    ret.append(queue[0])
    i+=1
print(ret)
