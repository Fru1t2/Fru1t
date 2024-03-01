import sys

a ,b = map(int, sys.stdin.readline().split())
arr1 = [sys.stdin.readline().strip() for i in range(a)]
arr2 = [sys.stdin.readline().strip() for j in range(b)]

set_arr1 = set(arr1)
set_arr2 = set(arr2)
result = list(set_arr1 & set_arr2)


print(len(result))
result.sort()
for i in result:
    print(i, end="\n")
