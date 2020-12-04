# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Looking at the second condition we can use the double binary search approach. 
# which will result in a time complexity of O(log(m)+log(n))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

number=int(input('Enter the number to find here: '))

# This function will return an array in which the value is supposed to be present

def endbinary(matrix,number):
    length=len(matrix)
    if length>1:
        middle=length//2
        if matrix[middle][-1]>=number and matrix[middle-1][-1]<number:
            return matrix[middle]
        elif matrix[middle][-1]<number:
            return endbinary(matrix[middle:],number)
        else:   return endbinary(matrix[:middle],number)
    else:
        return matrix[0]

array=endbinary(matrix,number)
def binary(array,number):
    length=len(array)
    if length==1:
        if array[0]==number:
            return True
        return  False
    else:
        middle=length//2
        if array[middle]==number:
            return True
        elif array[middle]>number:
            return binary(array[:middle],number)
        else:
            return binary(array[middle:],number)
    
print(binary(array,number))