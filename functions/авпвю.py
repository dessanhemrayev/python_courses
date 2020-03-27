def modify_list(l):
    i = 0
    while i < len(l):
        if not(l[i]%2):
            l[i] =int(l[i]/ 2)
            i += 1
        else:
            del l[i]
    return None

lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
print(lst)  