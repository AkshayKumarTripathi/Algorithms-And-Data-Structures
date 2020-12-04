# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


# This is the Dynamic programming solution in which I have used backtracking (Efficient approach is below).

rows=int(input('Enter the Number of Rows: '))
cols=int(input('Enter the number of columns here : '))


# table=[[-1]*cols for _ in range(rows)]
# def total(start_r,start_c,end_r,end_c,table):
    
#     if isvalid(start_r,start_c,end_r,end_c):
#         if start_r==end_r and start_c==end_c:
#             return 1
#         else:
#             if table[start_r][start_c]==-1:
#                 right=total(start_r,start_c+1,end_r,end_c,table)
#                 down=total(start_r+1,start_c,end_r,end_c,table)
#                 table[start_r][start_c]=right+down
#                 return right+down
#             return table[start_r][start_c]
#     else:   return 0
# def isvalid(i,j,maxi,maxj):
#     if i>maxi or j>maxj:
#         return False
#     return True

# print(total(0,0,rows-1,cols-1,table))


            
# Second appraoch using combinations


# total=cols+rows-2

# n=d=1
# if cols<rows:
#     for _ in range(cols-1):
#         cols-=1
#         n*=total
#         d*=cols
#         total-=1
# else:
#     for _ in range(rows-1):
#         rows-=1
#         n*=total
#         d*=rows
#         total-=1
# print(n//(d))
