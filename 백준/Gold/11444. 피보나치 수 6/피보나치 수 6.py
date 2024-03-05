import sys
from math import sqrt


N = int(sys.stdin.readline())

def matrix_mul(A, B):
    N = len(A) # A의 행의 개수
    M = len(B[0]) # B의 열의 개수
    K = len(B) # B의 행의 개수 (또는 A의 열의 개수)

    # 결과를 저장할 행렬 초기화
    result = [[0]*M for _ in range(N)]

    # 행렬 곱셈 수행
    for i in range(N):
        for j in range(M):
            for k in range(K):
                result[i][j] += A[i][k] * B[k][j] % 1000000007
            result[i][j] %= 1000000007
    return result

def identity(N):
    return [[1 if i==j else 0 for j in range(N)] for i in range(N)]

def proof(A, B, N):
    if B == 0:
        return identity(N)
    elif B % 2 == 1:
        return matrix_mul(A, proof(A, B-1, N))
    else:
        half_power = proof(A, B//2, N)
        return matrix_mul(half_power, half_power)

alist = [[1, 1],[1, 0]]
blist = [[1],[1]]

if N == 1:
    print("1")
elif N == 2:
    print("1")
elif N == 3:
    print("2")
else:
    result = proof(alist, N-2, len(alist))
    output = matrix_mul(result, blist)
    print(output[0][0])