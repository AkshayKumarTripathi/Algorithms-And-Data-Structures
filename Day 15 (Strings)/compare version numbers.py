# Given two version numbers, version1 and version2, compare them.

# Version numbers consist of one or more revisions joined by a dot '.'. 
# Each revision consists of digits and may contain leading zeros. 
# Every revision contains at least one character. 
# Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. 
# For example 2.5.33 and 0.1 are valid version numbers.

# To compare version numbers, compare their revisions in left-to-right order. 
# Revisions are compared using their integer value ignoring any leading zeros. 
# This means that revisions 1 and 001 are considered equal. 
# If a version number does not specify a revision at an index, then treat the revision as 0. 
# For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.


version1 = "1.0.1"
version2 = "1"

i=j=0
len1=len(version1)
len2=len(version2)

v1=[]
v2=[]
temp=''
for x in range(len1):
    if version1[x]!='.':
        temp+=version1[x]
    else:
        v1.append(int(temp))
        temp=''

v1.append(int(temp))

temp=''
for x in range(len2):
    if version2[x]!='.':
        temp+=version2[x]
    else:
        v2.append(int(temp))
        temp=''

v2.append(int(temp))
print(v1)
print(v2)
len1=len(v1)
len2=len(v2)
while i<len1 and j<len2:
    if v1[i]<v2[j]:
        print(-1)
        break
    elif v1[i]>v2[j]:
        print(+1)
        break

    i+=1
    j+=1

# EK loop chalao , if i!=len1 then only 2 cases are possible that are either we will get 0 or we will get 1
# yaa toh 2.0.0 and 2 ho yaa phir 2.0.1 and 2 ho and vice versa for second case yeh logic laga ke pata karle

if i!=len1:
    while i<len1:
        if v1[i]>=1 :
            print(1)
        i+=1

    print(0)

elif j!=len2:
    while j<len2:
        if v2[j]>=1:
            print(-1)
        j+=1

    print(0)

else:
    print(0)
