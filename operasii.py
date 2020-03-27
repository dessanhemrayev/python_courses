a = float(input())
b = float(input())
op = input()
if "+" == op:
    print(a + b)
if "-" == op:
    print(a - b)
if "/" == op:
    if b == 0:
        print("Деление на 0!")
    else:
        print(a / b)
if "*" == op:
    print(a * b)
if "mod" == op:
    if b == 0:
        print("Деление на 0!")
    else:
        print(a % b)
if "pow" == op:
    print(a ** b)
if "div" == op:
    if b == 0:
        print("Деление на 0!")
    else:
        print(a // b)
