import math 
a = float(input()) 
b = float(input()) 
c = float(input()) 
if a == 0 and b == 0 and c == 0:
    print('3')
d = b ** 2 - 4 * a * c 
if d < 0: 
    print("0") 
x1 = (-b + pow(d, 0.5)) / 2 * a 
x2 = (-b - pow(d, 0.5)) / 2 * a 
if d > 0: 
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0: 
        x1 = int(x1) 
        x2 = int(x2) 
    if x1 > x2: 
        print("2", int(x2), int(x1)) 
    elif x2 > x1: 
        print("2", int(x1), int(x2))
    else:
        if x1 >x2: 
            print("2", float(x2), float(x1)) 
        elif x2 > x1: 
            print("2", float(x1), float(x2)) 
if a != 0 and b != 0 and c != 0 and d == 0 and x1 % 2 == 0: 
    if x1 % 2 ==0 and x2 % 2 == 0: 
        print("1", int(x1)) 
    else: 
        print("1", float(x1))