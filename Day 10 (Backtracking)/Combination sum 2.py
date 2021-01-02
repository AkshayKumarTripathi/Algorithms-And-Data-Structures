# Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.


candidates = [3,1,3,5,1,1]
target = 8
candidates.sort()
sol={}
for x in candidates:
    if x in sol.keys():
        sol[x]+=1

    else:   sol[x]=1
result=[]
def work(candidates,target,sol,temp=[],i=0):
    if target==0:
        result.append(temp[:])
        return None

    else:
        prev=-1
        for x in candidates[i:]:
            if prev!=-1 and prev==x:
                i+=1                                    
                #This i+1 is there because if we skip without it once the same numbers stop appearing the loop will begin from the previous 
                # i try to run this code without i+=1 and see there will be an extra pair of 5,3 with 3,5.
                continue
            prev=x
            if target-x<0:
                break
            else:
                target-=x
                temp.append(x)
        
                i+=1
                work(candidates,target,sol,temp,i) 
                target+=x
                temp.pop()
                

        return None

work(candidates,target,sol)
print(result)
