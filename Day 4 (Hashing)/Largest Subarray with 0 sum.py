array=[1, 0, 3]

# we have to find the length of the longest sub string with 0 sum
# The brute force approach is easy O(N**2) approach generating all the sub arrays and then verifying them I will directly solve with the 
# optimal approach.

record={}
length=0
sumation=0
index=0
for x in array:
    sumation+=x
    if sumation in record.keys():
        length=max(length,index-record[sumation])
        
    else:   record[sumation]=index
    index+=1
    

print(length)