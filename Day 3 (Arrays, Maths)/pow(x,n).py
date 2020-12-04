# Calculate the power of x**n

x=float(input('Enter the number (BASE): '))
n=int(input('enter the power: '))

negative=False
if n<0:
    negative=True
    n=-n

def power(x,n):
    if n==0:
        return 1
    else:
        if n%2==0:
            ans=power(x,n//2)
            return ans*ans
        else:
            ans=power(x,n//2)
            return x*ans*ans
pri=power(x,n)
if negative:
    pri=1/pri

print(pri)