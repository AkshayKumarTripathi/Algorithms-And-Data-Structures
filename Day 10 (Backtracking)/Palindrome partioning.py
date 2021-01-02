# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

s='cdd'
result=[]
def part(s,start=0,temp=[]):
    if start==len(s):
        result.append(temp[:])
        return None

    else:
        for x in range(start,len(s)):
            s_temp=s[start:x+1]
            if s_temp==s_temp[::-1]:
                temp.append(s_temp)
                part(s,x+1,temp)
                temp.pop()                 # very important step try writing this code again #
            
        return None


part(s)
print(result)