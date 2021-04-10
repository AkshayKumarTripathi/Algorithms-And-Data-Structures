coins = [2,5,10,1]#[186,419,83,408]
amount = 27

table = [[-1 for _ in range(amount+1)] for _ in range(len(coins)+1)]


def possible(i=len(coins),amt=amount,c=0):
    if table[i][amt]!=-1:
        return table[i][amt]
    
    if amt==0:
        return c

    if i==0:
        return amount+1
        
    if amt-coins[i-1]>=0:
        temp=min(possible(i,amt-coins[i-1],c+1)  ,  possible(i-1,amt,c))
        table[i][amt]=temp
        return temp
    
    temp=possible(i-1,amt,c)
    table[i][amt]=temp
    return temp



ans=possible()
if ans>amount:
    print('NO')
else:   print('YES')
print(ans)

