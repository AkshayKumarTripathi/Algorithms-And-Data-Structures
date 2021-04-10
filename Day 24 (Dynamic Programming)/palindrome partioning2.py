s='aaba'
length=len(s)
table=[[-1]*length for _ in range(length)]

def ans(i=0,j=length-1):
    if table[i][j]==-1:
        if i>=j:
            return 0
        if s[i:j+1]==s[i:j+1][::-1]:
            table[i][j]=0
            return 0
        ret=length+1
        for k in range(i,j):
            temp= ans(i,k) + 1 + ans(k+1,j)
            ret=min(ret,temp)
        table[i][j]=ret
        return ret

    return table[i][j]

print(ans())
