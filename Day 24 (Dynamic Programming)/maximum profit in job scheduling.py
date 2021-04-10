startTime = [1,2,3,4,6] ;endTime = [3,5,10,6,9]; profit = [20,20,100,70,60]

new = sorted( zip(startTime,endTime,profit) , key= lambda x : x[1])

length=len(profit)
table=[-1]*length

def solve(start=length-1):
    if start==-1:
        return 0

    if table[start]==-1:
        curr=new[start]
        temp=start
        while temp>=0 and new[temp][1] > curr[0]:
            temp-=1
        table[start] = max( solve(temp) + curr[2], solve(start-1)) 
    return table[start]

print(solve())