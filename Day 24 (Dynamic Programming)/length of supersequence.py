a='geek'
b='eke'

len1=len(a)
len2=len(b)

table=[[-1 for _ in range(len2+1)] for _ in range(len1+1)]

def lcs(len1=len1,len2=len2):
    if len1==0 or len2==0:
        return 0

    if table[len1][len2]!=-1:
        return table[len1][len2]    

    if a[len1-1]==b[len2-1]:
        table[len1][len2]=lcs(len1-1,len2-1)+1
        return table[len1][len2]
    
    table[len1][len2]=max(lcs(len1-1,len2),lcs(len1,len2-1))
    return table[len1][len2]


print(len1+len2-lcs())
    
    