a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    if b >= c:
        print(a)
        print(c)
        print(b)
    else:
        print(a)
        print(b)
        print(c)
if b > a and b >= c:
    if c >= a:
        print(b)
        print(a)
        print(c)
    else:
        print(b)
        print(c)
        print(a)
if c > a and c> b:
    if a >= b:
        print(c)
        print(b)
        print(a)
    else:
        print(c)
        print(a)
        print(b)
