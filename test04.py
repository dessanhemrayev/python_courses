a = [int(i) for i in input().split()]
b = sorted(a)
i = 0
k = 0
kl = 0
c = ''
while (i < len(a)):
    if b.count(b[i]) == 1:
        i+=1
        continue
    else:
        c += str(b[i]) + ' '
        i += b.count(b[i])

print(c)
