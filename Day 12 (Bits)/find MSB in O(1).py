num=int(input('Enter the number to compute: '))
count=0
for i in range(32):
    if (1<<i & num )!=0:
        count=i

print(1<<count)

    