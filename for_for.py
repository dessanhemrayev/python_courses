n = int(input())
k = 0
for i in range(1,n+1):
    for j in range(i):
        k += 1
        if k > n:
            break        
        elif k<=n:
            print(i, end=' ')
