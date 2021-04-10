# find the median of a matrix if in the matrix every row is sorted.

# We know that the median is at the middle,  if len is 9 i.e. there are 4 elements greater than or equal to and 4 less than or equal to.
# suppose this is the array 
# [1,2,3],
# [3,3,3],
# [3,3,3]
# we know that the median will lie between 1(min) and 3(max) (both inclusive) so we generate an array bwn 1 and 3 [1,2,3]
# now we will see if the median of generated array is the median in the matrix we apply binary search in every row and see the number of
# elements smaller than and equal to 2 we see that only 2 elements satisfy the condition so we set our condition to increase our low to mid +1
# once the high and low meets we can for sure say that this is the mumber which is the median.


matrix=[
    [1,2,3],
    [3,3,3],
    [3,3,3]
    ]

