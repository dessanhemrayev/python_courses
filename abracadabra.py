s="abracadabra"
s1=' '
s2=''
k=-1
d = len(s)
while d>0:
    for i in range(d):
        s2+=s[i]
    k+=1
    print(s1*k,s2)
    s2=''
    d-=1