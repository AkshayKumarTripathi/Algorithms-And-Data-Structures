text1 = "abc"
text2 = "def"
i=len(text1)
j=len(text2)

table=[[-1 for _ in range(j+1)] for _ in range(i+1)]

def find(text1=text1, text2=text2, i=i, j=j):
    if table[i][j]!=-1:
        return table[i][j]

    if i==0 or j==0:
        return 0

    if text1[i-1]==text2[j-1]:
        table[i][j]=find(text1,text2,i-1,j-1) + 1
        return table[i][j]
    
    table[i][j]=max(find(text1,text2,i-1,j) , find(text1,text2,i,j-1))
    return table[i][j]

print(find())


# For Printing the longest common subsequence

# text1 = "abcde"
# text2 = "ace"
# i=len(text1)
# j=len(text2)

# table=[[-1 for _ in range(j+1)] for _ in range(i+1)]

# def find(text1=text1, text2=text2, i=i, j=j):

#     if table[i][j]!=-1:
#         return table[i][j]

#     if i==0 or j==0:
#         return ""

#     if text1[i-1]==text2[j-1]:
#         table[i][j]=find(text1,text2,i-1,j-1) + text1[i-1]
#         return table[i][j]

#     temp1=find(text1,text2,i-1,j)
#     temp2=find(text1,text2,i,j-1)
#     if len(temp1)>len(temp2):
#         table[i][j]=temp1
#     else:   table[i][j]=temp2
#     return table[i][j]

# print(find())
