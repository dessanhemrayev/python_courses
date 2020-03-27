s = "aaaabbcaa"
s += ' '
k = 0
lk = 0
c = ""
d = len(s) - 1
i = 0
while (i<d):
    for j in range(lk, d):
        if (s[i] == s[j]):
            k += 1
        else:
            break
    if k==0:
        k=1
    c+= s[i] + str(k)
    i += k
    lk += k
    k = 0
print(c)
