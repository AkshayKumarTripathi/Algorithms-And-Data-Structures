rod=8
price = [5,5,7,3,11,16,16,20]
length=len(price)
table=[[-1 for _ in range(rod+1)] for _ in range(length+1) ]

def cut(i=length, rem=rod,p=0):
    if table[i][rem]!=-1:
        return table[i][rem]
    
    if i==0:
        return p
    if rem==0:
        return p

    new_cut=price[i-1]
    if rem-i>=0:
        temp=max(cut(i,rem-i,p+new_cut),cut(i-1,rem,p))
        table[i][rem]=temp
        return temp
    temp=cut(i-1,rem,p)
    table[i][rem]=temp
    return temp
    
print(cut())