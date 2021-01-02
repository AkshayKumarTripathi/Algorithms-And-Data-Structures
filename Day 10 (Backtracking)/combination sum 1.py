# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


candidate=[2,7,6,3,5,1]
target=9
sol=[]
candidate.sort()
def work(candidate,target,sol,temp=[],i=0):
    if target==0:
        sol.append(temp[:])
        return None
    else:
        for x in candidate[i:]:
            if target-x<0:
                continue
            else:
                target-=x
                temp.append(x)
                
                work(candidate,target,sol,temp,i)
                i+=1
                
                target+=x
                temp.pop()

        return None

work(candidate,target,sol,temp=[],i=0)
print(sol)



