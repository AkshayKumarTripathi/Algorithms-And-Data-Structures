# Given a non negative integer number num.
# For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

num=int(input('Enter The Number : '))
ret=[]
for n in range(num+1):
    count=0
    for i in range(32):
        if (1 << i & n):
            count+=1
    ret.append(count)

print(ret)