def update_dictionary(d, key, value):
    if d.get(key) == key:
        d.update({key: [value]})
    elif d.get(2 * key) == None:
        d.update({2 * key: [value]})
    else:
        d[2 * key] = [value]



x = {}
update_dictionary(x, 1, -1)
print(x)
update_dictionary(x, 2, -2)
print(x)
update_dictionary(x, 1, -3)
print(x)