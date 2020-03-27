a = [int(i) for i in input().split()]
min = a[0]
for i in range(len(a)):
    if int(a[i])<min:
        min = int(a[i])
print(min)
