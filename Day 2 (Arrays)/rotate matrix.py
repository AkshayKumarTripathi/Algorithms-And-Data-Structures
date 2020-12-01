# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
#  DO NOT allocate another 2D matrix and do the rotation.

# O(n**2) time complexity and O(n**2) space complexity

matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

# for x in matrix:
#     print(x)
# length=len(matrix)
# row=0
# column=length
# new=[[0 for _ in range(length)] for _ in range(length)]

# for rows in matrix:
#     column-=1
#     row=0
#     for item in rows:
#         new[row][column]=item
#         row+=1
# print()
# print()

# for x in new:
#     print(x)


# O(n**2) time complexity and O(1) space complexity

length=len(matrix)

for x in range(length):
    for y in range(x,length):
        matrix[x][y],matrix[y][x]=matrix[y][x],matrix[x][y]
    
for x in range(length):
    matrix[x]=matrix[x][::-1]
for x in matrix:
    print(x)

