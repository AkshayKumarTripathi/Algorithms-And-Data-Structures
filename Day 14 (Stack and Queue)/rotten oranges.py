# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has 
# a fresh orange. If this is impossible, return -1.

grid = [[2,1,1],[0,1,1],[1,0,1]]
if grid==[]:
    print(-1)
rows=len(grid)
cols=len(grid[0])
x_moves=[0,0,-1,1]
y_moves=[1,-1,0,0]
fresh_rem=0
time=0
arr=[]
for x in range(rows):
    for y in range(cols):
        if grid[x][y]==1:
            fresh_rem+=1
        elif grid[x][y]==2:
            arr.append([x,y])

def isvalid(x,y):
    if 0<=x<rows and 0<=y<cols:
        return True
    return False

def next(arr):
    ret=[]
    temp=0
    length=len(arr)
    while temp<length:
        x,y=arr[0]

        for i in range(4):
            if isvalid(x+x_moves[i],y+y_moves[i]) and grid[x+x_moves[i]][y+y_moves[i]]==1:
                ret.append([x+x_moves[i],y+y_moves[i]])
                grid[x+x_moves[i]][y+y_moves[i]]=2
        temp+=1
        arr.pop(0)
    return ret

while arr!=[]:
    if fresh_rem==0:
        break
    time+=1
    get_rotten=[]
    get_rotten=next(arr)
    fresh_rem-=len(get_rotten)
    arr+=get_rotten

if fresh_rem==0:
    print(time)
else:   print(-1)
