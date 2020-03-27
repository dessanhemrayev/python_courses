def IsPointInSquare(a, b):
    return a <= 1 and b <= 1
a = float(input())
b = float(input())
if IsPointInSquare(a, b) == True:
    print('YES')
else:
    print('No')
