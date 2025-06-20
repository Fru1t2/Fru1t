import sys

N = int(sys.stdin.readline())
is_prime = [True for _ in range(N + 1)]
is_prime[0] = is_prime[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

prime_list = [i for i, val in enumerate(is_prime) if val]
start, end, value, answer = 0, 0, 0, 0
if N == 1:
    print("0")
    exit(0)
while value < N:
    value += prime_list[end]
    end += 1
    if end < len(prime_list) and value + prime_list[end] >= N:
        value += prime_list[end]
        end += 1
        break

while True:
    if value >= N:
        if value == N:
            answer += 1
        value -= prime_list[start]
        start += 1
    elif end == len(prime_list):
        break
    else:
        value += prime_list[end]
        end += 1


print(answer)