N = int(input())
my_list = [input() for _ in range(N)]
output = 0
for j in range(N):
    storage = ""
    for i in range(len(my_list[j])):
        if i == 0 or my_list[j][i] != my_list[j][i-1]:
            if my_list[j][i] in storage:
                output -= 1
                break
            else:
                storage += my_list[j][i]
    output += 1

print(output)