# Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.




matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target=int(input('enter the number to find here : '))

#This approach is uses O(m+n) time complexity
rows=0

ro=len(matrix)
co=len(matrix[0])

cols=co-1

while True:
    if rows<0 or cols<0 or rows>=ro or cols>=co:
        print('Number is not present')
        break
    else:
        if matrix[rows][cols]==target:
            print('Yes! The number is present')
            break
        elif matrix[rows][cols]<target:
            rows+=1
            continue
        else:
            cols-=1
            continue
            
