# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

word1 = "akshay"
word2 = "kumar"
w1=len(word1)
w2=len(word2)

table=[[x+i for x in range(w2+1)] for i in range(w1+1)]

for i in range(1,w1+1):
    for j in range(1,w2+1):
        if word1[i-1]==word2[j-1]:
            table[i][j]=table[i-1][j-1]
        else:   table[i][j] = min(table[i-1][j],table[i-1][j-1],table[i][j-1]) + 1
    
print(table[w1][w2])