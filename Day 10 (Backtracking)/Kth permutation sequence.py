# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.


n=int(input('Enter the value for N: '))
k=int(input('enter the value of k: '))

nums=[str(n) for n in range(1,n+1)]
fact=[]
temp=1
for x in range(1,n+1):
    temp=temp*x
    fact.append(temp)

[1,2,6,24]

s=''

while k>1:
    block_size=fact[n-2]
    index=k//block_size 
    index=index-1 if k%block_size==0 else index
    s+=(nums[index])
    nums.pop(index)
    n-=1
    k-=index*block_size

s+=''.join(nums)
print(s)