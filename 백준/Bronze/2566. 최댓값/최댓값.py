arr1 = []
for i in range(9):
    arr1.append(list(map(int, input().split())))

high = 0
for i in range(9):
    for j in range(9):
        if arr1[i][j] > high:
            high = arr1[i][j]

print(high)
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        if arr1[i][j] == high:
            print(i+1, j+1)
            break