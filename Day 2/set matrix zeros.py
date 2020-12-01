# Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

# Follow up:

# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
replacement=[0]*len(matrix[0])
row=-1
zeros=[]
for x in matrix:
    col=0
    row+=1
    for new in x:
        if new==0:
            zeros.append([row,col])
        col+=1
for x in zeros:
    matrix[x[0]]=replacement
    for new in matrix:
        new[x[1]]=0

for x in matrix:
    print(x)