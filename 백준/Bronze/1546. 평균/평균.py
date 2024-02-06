length = int(input())
my_list = list(map(int, input().split()))
high = 0
sum = 0

for i in range(length):
    if my_list[i] > high:
        high = my_list[i]

for j in range(length):
    my_list[j] = (my_list[j] / high) * 100

for k in range(length):
    sum += my_list[k]

print(sum / length)