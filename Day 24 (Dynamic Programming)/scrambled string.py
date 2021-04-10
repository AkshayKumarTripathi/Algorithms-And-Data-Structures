a="abc"
b="bac"


length=len(a)

if length!=len(b):
    print('These are not scrambled strings!!!')

record={}

def ans(a : str = a , b : str = b , length : int = length):

    if a + ' ' + b in record.keys():
        return record[a + ' ' + b]

    if length==1:
        return a==b
    
    if a == b:
        return True

    for k in range(1,length):
        n1=record.get(a[:k] + ' ' + b[length-k:] , ans( a[:k] , b[length-k: ] , k))
        if n1:
            record[a[:k] + ' ' + b[length-k:]]=True
            n2=record.get(a[k:] + ' ' + b[:length-k],ans( a[k:] , b[:length-k] , length-k ))
            if n2:
                record[a[k:] + ' ' + b[:length-k]] = True
                return True
            else:   record[a[k:] + ' ' + b[:length-k]] = False
            
        else:   record[a[:k] + ' ' + b[length-k:]]=False

        e1=record.get(a[:k] + ' ' + b[:k],ans(a[:k] , b[:k] , k))
        if e1:
            record[a[:k] + ' ' + b[:k]]=True        
            e2=record.get(a[k:] +' '+ b[k:],ans(a[k:] , b[k:] , length-k))
            if e2:
                record[a[k:] +' '+ b[k:]]=True
                return True
            else:   record[a[k:] +' '+ b[k:]]=False
        else:   record[a[:k] + ' ' + b[:k]]=False  
    return False

print(ans())