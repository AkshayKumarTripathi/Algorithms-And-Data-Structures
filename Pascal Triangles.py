# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# I Know this problem can be solved more efficiently using DP but I have not studied it yet so I will update it later

numRows=int(input('Enter the number here: '))
ret=[[1],[1,1]]
if numRows<=2:
    if numRows==0:
        print([])
    else:   print(ret[:numRows])
else:
    run=1
    for x in range(numRows-2):
        give=[]
        
        upper=ret[-1]
        mover=0
        for temp in range(run):
            temp_no=upper[mover]+upper[mover+1]
            mover+=1
            give.append(temp_no)
        give=[1]+give+[1] 
        ret.append(give)
        run+=1
    for x in ret:
        print(x)