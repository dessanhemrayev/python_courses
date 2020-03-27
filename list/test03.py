a = [int(i) for i in input().split()]
b=''
if len(a) == 1:
    print(a)
elif len(a) != 1: 
        for i in range(len(a)):
            if i-1<len(a) and i+1<len(a):
                b += str(a[i-1]+a[i+1])+' '
            else:
                b += str(a[i-1]+a[0-i-1])
print(b)