length = int(input())
arr = list(map(int, input().split()))
wanttofind = int(input())
gang = 0

for i in range(length):
    if arr[i] == wanttofind:
        gang += 1

print(gang)
        