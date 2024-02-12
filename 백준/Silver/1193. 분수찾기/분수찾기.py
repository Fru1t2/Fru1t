n = int(input())
a = 1

while n > a:
    n -= a
    a += 1

if a % 2 == 0:
    up = n
    down = a - n + 1
else:
    up = a - n + 1
    down = n

print(up,'/',down, sep="")