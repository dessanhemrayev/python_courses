import copy
a=[]
while True:
    raw=input()
    if raw=="end":
        break
    str=[[int(i) for i in raw.split()]]
    a[len(a):]=str
a1=copy.deepcopy(a)
for j in range(0,len(a)):
    for i in range(0,len(a[0])):
        a1[j][i]=0
        for dj in 1, -1:
            if j+dj<0:
                j1=len(a)
            elif j+dj==len(a):
                j1=-1
            else:
                j1=j
            a1[j][i]+=a[j1+dj][i]
        for di in 1, -1:
            if i+di<0:
                i1=len(a[0])
            elif i+di==len(a[0]):
                i1=-1
            else:
                i1=i
            a1[j][i]+=a[j][i1+di]
 
for j in range(len(a1)):
    for i in range(len(a1[j])):
        
        print(a1[j][i],end=' ')
    print()
