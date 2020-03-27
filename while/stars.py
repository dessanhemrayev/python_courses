
i = 0
stars = "*"
while i < 5:
    print('*')
    stars += '*'
    if i % 2 == 0:
        print('**')
        stars += '**'
    if i > 2:
        print('***')
        stars += '***'
    i = i + 1
print(len(stars)-1)

