# Given a string s, return the longest palindromic substring in s.

# we are going to start from the middle and then expand in both the directons if we 
# find a match we continue else break.


s="racecar"
length=len(s)
start=end=0
curr=0
def helper(s,start,end):
    while start>=0 and end<length and s[start]==s[end]:
        start-=1
        end+=1
    return end-start-1

    
for x in range(length):
    temp=max(helper(s,x,x),helper(s,x,x+1))
    if temp>curr:
        curr=temp
        start=x-(temp-1)//2
        end=x+(temp)//2
print(s[start:end+1])


print(curr)



    