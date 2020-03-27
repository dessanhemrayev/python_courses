t1, t2 =1,1
# [int(x) for x in input().split()]
p, v, a =100,100,5
#[int(x) for x in input().split()]
pp, ppp, tp, ts, to = 0, 0, 0, 0, 0
prov = True

if p / v < t1:
    print('Pass')
else:
    tt = v / a
    pp = v * tt - (a * (tt **2)) / 2
    ppp = p - pp
    if ppp < 0:
        print('%.3f' % p, '%.3f' % (t2 - 1))
        prov = False
    tp = ppp / v + tt
    to = t1 + t2
    while prov:
        if p / v >= to and p / v < to + t1:
            print('Pass')
            prov = False
        elif tp < to:
            ts = to - tp
            if pp < 0.001:
                pp = 0.001
            if ts < 0.001:
                ts = 0.001
            print('%.3f' % pp, '%.3f' % ts)
            print("ffgffh")
            print(f"{pp:.3f} {ts:.3f}")
            prov = False
        else:
            to += (t1 + t2)
