# Inversion Count for an array indicates – how far (or close) the array is from being sorted. 
# If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
# Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j 


array=[3, 1, 2]

# Code for n**2 time complexity

# inversions=0
# length=len(array)
# for x in range(length):
#     current=array[x]
#     for y in range(x+1,length):
#         if array[y]<current:
#             inversions+=1
# print(inversions)


#This is the code for n(log(n)) approach I have used a slight modification in merge sort

def inversioncounter(array):
    if len(array)<=1:
        return array,0
    else:
        split=len(array)//2
        left,l_inv=inversioncounter(array[:split])
        right,r_inv=inversioncounter(array[split:])
        left_length=len(left)
        right_length=len(right)
        i=j=0
        total_inv=0
        new=[]
        while i!=left_length and j!=right_length:
            if left[i]<right[j]:
                new.append(left[i])
                i+=1
            else:
                new.append(right[j])
                total_inv+=(left_length-i)          # This is the variable which keeps the track of inversions happening
                j+=1
            
        if i!=left_length:
            new=new+left[i:]
            
        if j!=right_length:
            new+=right[j:]
        return new,total_inv+l_inv+r_inv


print(inversioncounter(array))


