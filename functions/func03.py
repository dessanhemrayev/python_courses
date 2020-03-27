a = [int(i) for i in input().split()]
k = 0
j = 0
d = len(a)
for i in range(d):
    if int(a[i]) % 2 == 1:
        k +=1
if k == d:
    print(end='')
else:
        while (j<d-k+1):
            if j>len(a)-1:
                break
            else:
                if int(a[j]) % 2 == 1:
                    a.remove(a[j])
                    j = -1
            j += 1
        for i in range(d-k):
            if int(a[i]) % 2 == 0:
                a[i]=int(a[i]/2)
        print(a)
          
