def modify_list(l):
    k = 0
    j = 0
    d = len(l)
    for i in range(d):
        if int(l[i]) % 2 == 0:
            k += 1
    if k == d:
        print(end='')
    else:
        while j < d - k + 1:
            if j > len(l) - 1:
                break
            else:
                if int(l[j]) % 2 == 1:
                    l.remove(l[j])
                    j = -1
            j += 1
    for i in range(k):
        if int(l[i]) % 2 == 0:
            l[i] = int(l[i] / 2)
