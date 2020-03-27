n = int(input())
if n % 100 != 11 and (n % 10 == 1 or n == 1 and n != 1):
   print(n, "программист")
if 1 < n % 10 < 5 and n % 100 != 11 and n % 100 != 12 and n % 100 != 13 and n % 100 != 14:
        print(n, "программиста")
if n > 10 and (11 <= n % 100 <= 14 ) or n % 10 == 0 or 4 < n % 10:
   print(n, "программистов")
