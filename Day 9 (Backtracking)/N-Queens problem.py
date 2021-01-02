# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, 
# respectively.

n=int(input('Enter the size of the board: '))
board = [['.' for _ in range(n)] for _ in range(n)]
solution=[]
seen=[['.' for _ in range(n)] for _ in range(n)]

ans=[]

def isValid(board,move):
    i,j=move
    n=len(board)
    for x in range(n):
        if board[i][x] =='Q' or board[x][j]=='Q':
            return False

    while i>0 and i<=n-1 and j>=0 and j<n-1:
        i-=1
        j+=1
        if board[i][j]=='Q':
            return False

    i,j=move

    while i>=0 and i<n-1 and j>0 and j<=n-1:
        i+=1
        j-=1
        if board[i][j]=='Q':
            return False
    
    i,j=move

    while i>=0 and i<n-1 and j>=0 and j<n-1:
        i+=1
        j+=1
        if board[i][j]=='Q':
            return False
    i,j=move
    while i>0 and i<=n-1 and j>0 and j<=n-1:
        i-=1
        j-=1
        if board[i][j]=='Q':
            return False

    return True


def start(board,ans,n,line=0):
    if n==0:
        temp=[]
        for x in board:
            temp.append(''.join(x))
        ans.append(temp)
        return None

    else:
        for x in range(len(board)):
            if isValid(board,(line,x)):
                board[line][x]='Q'
                n-=1
                line+=1
                start(board,ans,n,line)
                n+=1
                line-=1
                board[line][x]='.'
        return None
            

                





                    

        
                
start(board,ans,n)               
print(ans)
    

