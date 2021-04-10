a='heap'
b='pea'

len1=len(a)
len2=len(b)

table=[[0 for _ in range(len2+1)] for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if a[i-1]==b[j-1]:
            table[i][j]=table[i-1][j-1]+1

        else:   table[i][j]=max(table[i-1][j],table[i][j-1])

print('Delete {} chars from str1'.format(len1-table[len1][len2]))
print('insert {} chars in str1'.format(len2-table[len1][len2]))