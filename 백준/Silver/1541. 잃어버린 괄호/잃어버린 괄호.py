import sys

result = []
alist = list(sys.stdin.readline().split("-"))

for a in alist:
    blist = a.split("+")
    output = 0
    for b in blist:
        output += int(b)
    result.append(output)

value = result[0]
for i in range(1,len(result)):
    value -= result[i]

print(value)