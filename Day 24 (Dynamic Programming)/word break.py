word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
record = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

length=len(word)
table=[-1]*(length)
record=set(record)

def solve(i=0):
    if table[i]!=-1:
        return table[i]
    if i==length:
        return True
    for k in range(i,length):
        if word[:k+1] in record and solve(k+1):
            table[i] = True
            return True
    table[i] = False
    return table[i]

print(solve())