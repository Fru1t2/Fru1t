length = int(input())
arr = list(map(int, input().split()))
low = 1000000
high = -1000000


for i in range(length):
    if arr[i] < low:
        low = arr[i]
    if arr[i] > high:
        high = arr[i]

print(low, high)