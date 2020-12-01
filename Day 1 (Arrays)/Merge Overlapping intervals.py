arr=[[1,4],[4,5]]

# If we dont want to use the built in sort function we can use the following commented code which uses quick sort

# def quick(arr):                                    
#     if len(arr)<=2:
#         return arr
#     else:
#         left=[]
#         right=[]
#         pivot=arr[0]
#         for x in arr[1:]:
#             if x[0]<pivot[0]:
#                 left.append(x)
#             else:   right.append(x)
#         return quick(left)+[pivot]+quick(right)
#arr=quick(arr)
# for x in range(len(arr)-1):
#     if arr[x][0]==arr[x+1][0] and arr[x][1]>arr[x+1][1]:
#         arr[x],arr[x+1]=arr[x+1],arr[x]

arr.sort()
ret=[]
for new in arr:
    if len(ret)<1:
        ret.append(new)
    else:
        if ret[-1][1]>=new[0]:                          #[1,6][2,4] and [1,2][2,4]
            if ret[-1][1]>=new[1]:
                pass
            elif ret[-1][1]<new[1]:
                start=ret[-1][0]
                end=new[1]
                ret.pop()
                ret.append([start,end])
        else:   ret.append(new)

print(ret)


            
        
        
    

    





    
