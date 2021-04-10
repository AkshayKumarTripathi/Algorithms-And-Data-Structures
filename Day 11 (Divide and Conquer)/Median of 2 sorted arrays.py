nums1=[]
nums2=[2,3]

def median(nums1,nums2):
    new=[]
    total=len(nums1)+len(nums2)
    i=j=z=0
    if total%2!=0:
        total=total//2
        while i<len(nums1) and j<len(nums2) and z<=total:
            if nums1[i]<nums2[j]:
                new.append(nums1[i])
                i+=1
            else:
                new.append(nums2[j])
                j+=1
            z+=1 
            
        if z==total+1:
            return float(new.pop())
        
        if i<len(nums1) and z<=total:
            z+=1
            new.append(nums1[i])
            i+=1
        
        elif j<len(nums2) and z<=total:
            z+=1
            new.append(nums2[j])
            j+=1
            
        return float(new.pop())

    else:
        total=total//2 
        while i<len(nums1) and j<len(nums2) and z<=total:
            if nums1[i]<nums2[j]:
                new.append(nums1[i])
                i+=1
            else:
                new.append(nums2[j])
                j+=1
            z+=1 
            
        if z==total+1:
            one=new.pop()
            two=new.pop()
            return (one+two)/2
        
        print(j,z,total)
        while i<len(nums1) and z<=total:
            z+=1
            new.append(nums1[i])
            i+=1


        while j<len(nums2) and z<=total: 
            z+=1
            new.append(nums2[j])
            j+=1
            print(new)
            
        one=new.pop()
        two=new.pop()
        return (one+two)/2

print(median(nums1,nums2))