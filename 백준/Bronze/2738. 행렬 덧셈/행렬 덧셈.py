a, b = map(int, input().split())
arr1, arr2 = [], []
for i in range(a):
    arr1.append(list(map(int, input().split())))
for j in range(a):
    arr2.append(list(map(int, input().split())))

temp = []

for j in range(a):
    row = [x + y for x, y in zip(arr1[j], arr2[j])]
    temp.append(row)

for x in temp:
    print(*x, sep=' ')
