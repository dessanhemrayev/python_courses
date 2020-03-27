a = [int(i) for i in input().split()]
s = 0
#for i in a:
#  s += i
for i in range(int(len(a))):
    s += a[i]
print(s)