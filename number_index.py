lst = [int(i) for i in input().split()]
x = int(input())
l = 0
c = ''
k = 0
while (l<len(lst)):
    if lst[l]==x:
        c += str(l)+' '
        l +=1
        k += 1
    else:
        l +=1
if k==0:
    print("Отсутствует")
else:
    print(c)

        

