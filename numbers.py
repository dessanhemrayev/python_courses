from math import pow
fl = True
sum = 0
p = 0
while(fl):
    a = int(input())
    sum += a 
    p += a**2
    if sum == 0:
        fl = False
        print(p)