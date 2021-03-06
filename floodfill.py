image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
maxc=len(image)
maxr=len(image[0])
initial=[[sc,sr]]
look=image[sc][sr]

def isvalid(c,r):
    return c>=0 and r>=0 and c<maxc and r<maxr

def find(c,r):
    addc=[1,0,0,-1]
    addr=[0,1,-1,0]
    temp=[]
    for x in range(4):
        tempc=c+addc[x]
        tempr=r+addr[x]
        if isvalid(tempc,tempr) and image[tempc][tempr]==look:
            temp.append([tempc,tempr])
            
    return temp

while initial:
    c,r=initial.pop(0)
    temp=find(c,r)
    image[c][r]=newColor
    initial+=temp

for x in image:
    print(x)