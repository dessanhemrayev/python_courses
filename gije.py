#file = open("asd.txt",'r')
#line = ""
s = "J5V11N2X9f19E1P2K6q1Q7z12g12q6m4B2R10i7O10f20y10k12C3t7"
#for line in file:
#    s += line
#file.close()
s += ' '
k = 0
l = ''
k = 0
kl = ''
for i in range(len(s)):
    if '2' <= s[i] <= '99':
        k = int(s[i])
        l += s[i - 1] * (k)
    elif s[i] == '1':
        if i + 1 < len(s):
            if '0' <= s[i + 1] <= '99':
                kl = s[i] + s[i + 1]
                k = int(kl)
                l += s[i - 1] * (k)
                i += 2
            else:
                k = int(s[i])
                l += s[i - 1] * (k)
print(l)
with open("otwet.txt",'w') as ouf:
    ouf.write(l)
    ouf.write(str(400))