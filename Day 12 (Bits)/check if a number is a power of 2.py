# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x

# we are using the algorithm that if the numbers differ by one the binary representation of the smaller 
# can be obtained by flipping the right of the rightmost set bit (1){Including it self} of the greater numbeer.
# 
#  
# for ex 8 => 1000 and 7 => 0111 or 6 => 110 and 5 => 101 ie 1|10 => 1|01 see how we flipped the right of rightmost setbit.
# 


n=int(input('Enter The number :'))
if ((n) & (n-1)) == 0 and n!=0:
    print('Yes')
else:   print('No')