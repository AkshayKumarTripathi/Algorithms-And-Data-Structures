strs=["dog","racecar","car" ]
ret=''
a=False
i=0
while True:
    if i<len(strs[0]):
        char=strs[0][i] 
    else: break
    for x in strs[1:]:
        if i>=len(x) or char!=x[i]:
            a=True
            break
    if a:
        break
    i+=1

print(strs[0][:i])