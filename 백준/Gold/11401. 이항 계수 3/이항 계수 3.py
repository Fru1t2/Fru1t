N, K = map(int, input().split())
p = 1000000007


def factorial(N):
    n = 1
    for i in range(2, N + 1):
        n = (n * i) % p
    return n


def solving(N, K):
    if K == 0:
        return 1
    if K == 1:
        return N
    n = K // 2
    m = K % 2
    temp = solving(N, n)
    if m == 0:
        return (temp * temp) % p
    else:
        return (temp * temp * N) % p

a = factorial(N-K) * factorial(K)
b = factorial(N) % p
c = solving(a, p-2) % p
print((b * c)%p)
