base = 2
x = int(input())
digit = ''
print(bin(x))
while x>0:
    digit += str(x % base)
    x//=base
reversed(digit)
print(digit)
