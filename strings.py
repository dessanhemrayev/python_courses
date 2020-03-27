s = input()
k = 0
a = s.count('c')
b = s.count('C')
c = s.count('g')
d = s.count('G')
pros = (a+b+c+d) / len(s)
print(pros*100)