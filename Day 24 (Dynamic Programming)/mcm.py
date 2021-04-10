arr=[40, 20, 30, 10, 30]
length=len(arr)
def mcm(i=1,j=length-1):
    if i>=j:
        return 0
    ans=-1
    for k in range(i+1,j+1):
        temp = mcm(i,k-1) + mcm(k,j) + arr[i-1]*arr[k-1]*arr[j]
        if ans==-1:
            ans=temp
        else:   ans=min(ans,temp)

    return ans
    

print(mcm())