# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

terrain=[4,2,0,3,2,5]
lmax=[]
rmax=[]
ans=0
l=r=0
for x in terrain:
    if x<=l:
        lmax.append(l)
    else:
        l=x
        lmax.append(l)

for x in terrain[::-1]:
    if x<=r:
        rmax.insert(0,r)

    else:
        r=x
        rmax.insert(0,r)

for x in range(len(terrain)):
    ans = ans + min(lmax[x],rmax[x]) - terrain[x]


print(ans)