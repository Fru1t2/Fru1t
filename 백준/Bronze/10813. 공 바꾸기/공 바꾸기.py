N, M = map(int, input().split())
list = [i+1 for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    list[a-1], list[b-1] = list[b-1], list[a-1]

print(*list, end=" ")