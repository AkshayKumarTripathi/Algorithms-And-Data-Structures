deno=[10,20,50,100,200,500,2000]
value=70
pointer=len(deno)-1
ans=[]
count=0
while value!=0 and pointer>=0:
    if value<deno[pointer]:
        pointer-=1
    else:
        value=value-deno[pointer]
        ans.append(deno[pointer])
        count+=1

if pointer<0 or value!=0:
    print('Sommy bhai nahi ho sakta change')
else:   print(ans,count)