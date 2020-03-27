s = input().split()
str1 = ''
str2 = ''
for r in range(len(s)):
    if len(s[r]) > len(str1):
        str1 = s[r]
print(str1)
d=len(str1)-1
for i in range(d+1):
    str2+=str1[d-i]

print(str2)