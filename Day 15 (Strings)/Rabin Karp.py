haystack='Akshay and Akshay'
needle='Akshay'
hay_len=len(haystack)
needle_len=len(needle)
hash=0
lis=[]
need=0
for x in needle:
    needle_len-=1
    need+=ord(x)*(26**needle_len)

needle_len=len(needle)
for x in range(needle_len):
    temp=ord(haystack[x])*(26**(needle_len-x-1))
    hash+=temp
print(hash,need)

if hash==need and needle==haystack[:needle_len]:
    print(needle)

i=needle_len

while i<hay_len:
    hash=hash-ord(haystack[i-needle_len])*(26**(needle_len-1))
    hash*=26
    hash+=ord(haystack[i])
    if hash==need and needle==haystack[i-needle_len+1:i+1]:
        print(needle,i-needle_len+1)
        
    i+=1





