# Given a string s, find the length of the longest substring without repeating characters.

s = ""                      # Ans =3 string is abc

# The basic approach would be to create all sub arrays and check if the ssub-string has any repeting chars:


# I will directly jump to the optimal solution using hashing and two pointers front and back which will store the length of the subarray 
# with the current largest length.

record={}
front=back=length=0
for x in s:
    if x in record.keys():
        if record[x]+1>back:

            back=record[x]+1
        record[x]=front
        
    else:
        record[x]=front
    length=max(length,front-back+1)
    front+=1
print(length)
