nums=[2,6,4,1,3,1,5]
record=dict()
for x in nums:
    if x in record.keys():
        print(x)
        break
    else:   record[x]=0


# Floyds Al