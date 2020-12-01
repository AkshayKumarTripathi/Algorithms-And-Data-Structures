#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.


# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
nums1=[1,2,5]
nums2=[1,2,3,4,5,6,7,8,9]
m=len(nums1)
n=len(nums2)
new=[]
i=j=0
while i<m and j<n:
    one=nums1[i]
    two=nums2[j]
    if one<two:
        new.append(one)
        i+=1
    elif two<one:
        new.append(two)
        j+=1
    else:
        new.append(one)
        new.append(one)
        i+=1
        j+=1
if i!=m:
    new+=nums1[i:]
         
elif j!=n:
    new+=nums2[j:]

print(new)