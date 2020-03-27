file=open('685.txt', "r")
k = 0
for line in file:
    print(line)
    k+=1
file.close()
print(k)