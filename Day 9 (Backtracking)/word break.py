# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

# This is now the optimized approach once I learn DP I will solve it again.

s='catsandog'
wordDict = ["cats", "dog", "sand", "and",'an', "cat"]

def word(s,words,length,start=0):
    if start==length:
        return True       
    
    else:
        for x in range(len(words)):
            curr=words[x]
            curr_len=len(curr)
            if curr_len+start>length:
                continue
            elif s[start:start+curr_len]==curr:
                start+=curr_len
                if word(s,words,length,start)==True:
                    return True
                start-=curr_len
        return False      


print(word(s,wordDict,len(s)))
