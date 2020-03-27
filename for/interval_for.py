a = int(input())
b = int(input())
k = 0
s = 0
sred = 0
for i in range(a, b+1):
    if i % 3 == 0:
        k += 1
for l in range(a, b+1):
    if l % 3 == 0:
        s += l
print(s / k)
