a = 1
while a == 1:
    b = int(input())
    if b < 10:
        continue
    elif b > 100:
        break
    else:
        print(b)
