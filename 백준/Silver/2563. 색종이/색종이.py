n = int(input())
output = 0
temp = [list(map(int, input().split())) for _ in range(n)]
nlist = [[0 for i in range(101)] for j in range(101)]

for x, y in temp:
    for i in range(x, x+10):
        for j in range(y, y+10):
            nlist[i][j] = 1

for i in range(101):
    for j in range(101):
        output += nlist[i][j]

print(output)