op = input()
if "треугольник" == op:
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
if "прямоугольник" == op:
    a = int(input())
    b = int(input())
    print(a * b)
if "круг" == op:
    a = int(input())
    print(a**2*3.14)