import sys

N, B = map(int, sys.stdin.readline().split())

alist = []
for _ in range(N):
    alist.append(list(map(int, sys.stdin.readline().split())))

def matrix_mul(A, B, N):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j] % 1000
            result[i][j] %= 1000
    return result

def identity(N):
    return [[1 if i==j else 0 for j in range(N)] for i in range(N)]

def proof(A, B, N):
    if B == 0:
        return identity(N)
    elif B % 2 == 1:
        return matrix_mul(A, proof(A, B-1, N), N)
    else:
        half_power = proof(A, B//2, N)
        return matrix_mul(half_power, half_power, N)

for row in proof(alist, B, N):
    print(" ".join(map(str, row)))