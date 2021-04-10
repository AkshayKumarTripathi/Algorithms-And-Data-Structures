amount = 5
coins = [2,5,10,1]
table = [[-1 for _ in range(amount+1)] for _ in range(len(coins)+1)]

def count(i=len(coins),amt=amount):
    if table[i][amt]!=-1:
        return table[i][amt]
    
    if amt==0:
        return 1
    if i==0:
        return 0

    
    if amt-coins[i-1]>=0:
        temp= count(i,amt-coins[i-1]) + count(i-1,amt)
        table[i][amt]=temp
        return temp
    temp=count(i-1,amt)
    table[i][amt]=temp
    return temp

print(count())

