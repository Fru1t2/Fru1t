import sys

a = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(a)]
def custom_sort(item):
    return(len(item), item)
data = list(set(data))
data.sort(key = custom_sort)
for i in data:
    print(i, end='\n')