def f(x):
    if x <=-2:
        return 1-(x+2)**2
    elif 2 < x:
        return ((x-2)**2)+1
    elif -2 < x <= 2:
        return -x/2 

a = float(input())
print(f(a))