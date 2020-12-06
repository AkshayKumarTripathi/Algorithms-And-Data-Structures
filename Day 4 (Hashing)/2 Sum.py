array=[1,2,3,4,5,6,7,89,7,3,2,4,5,1,23,4,5,12,32,0,14,6,8,5,9,11]
record={}
ret=[]
target=14
for x in array:
    if x in record.keys():
        ret.append((x,target-x))
        del record[x]
    else:
        record[14-x]=x

print(ret)