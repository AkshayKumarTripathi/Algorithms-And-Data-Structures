# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero, which means losing its fractional part. 
# For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

# Note:

# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:
# [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

num = int(input('Enter the number: '))
div = int(input('Enter the divisor: '))
neg=False
if not (num<0 and div<0) and (num<0 or div<0):
    neg=True
num=abs(num)
div=abs(div)
res=0
while num>=div:
    start=0
    while (num-(div*(1<<start))) >=0:
        start+=1
    start = start-1 if start>0 else 0    
    res+=1<<start
    num=num-(div*(1<<start))
if neg:
    res=abs(res)
print(res)
    