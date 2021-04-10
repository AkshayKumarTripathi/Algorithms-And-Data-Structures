# Find the nth root of a number
x=float(input('Enter the number: '))
root=int(input('Enter the root val: '))
acc=0.0000000001
if x<1 and x>0:
    high=1
    low=x
    guess=(high+low)/2
    while abs(guess**root-x)>=acc:
        if guess**root>x:
            high=guess
        else: low=guess
        guess=(high+low)/2

    print(guess)    

elif x>1:
    high=x
    low=1
    guess=(high+low)/2
    while abs(guess**root-x)>=acc:
        if guess**root>x:
            high=guess
        else: low=guess
        guess=(high+low)/2

    print(guess)


elif x==0:
    print(0)

elif x==1:
    print(1)