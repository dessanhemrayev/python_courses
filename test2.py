def example(t1: int, t2: int, p: int, v: int, a: int) -> str:
    if p / v % (t1 + t2) - t1 < 0:
        return "Pass"
    s = v**2 / (2 * a)
  
    t = t2 + t1 - ((s - p) / v + v / a) % (t1 + t2)
    return f"{s:.3f} {t:.3f}"





print(example(1,1,100,100,5))