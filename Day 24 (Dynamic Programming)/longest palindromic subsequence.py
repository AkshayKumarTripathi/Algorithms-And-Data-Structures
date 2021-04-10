text1 = "geek"
text2 =text1[::-1]
i1=len(text1)
j1=len(text2)

table=[[0 for _ in range(j1+1)] for _ in range(i1+1)]

for i in range(1,i1+1):
    for j in range(1,j1+1):
        if text1[i-1]==text2[j-1]:
            table[i][j]=table[i-1][j-1]+1
        else:   table[i][j]=max(table[i-1][j],table[i][j-1])

print(table[i1][j1])

