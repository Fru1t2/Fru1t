import sys

A, B, C = map(int, sys.stdin.readline().split())
def solve(A, B):
    if B == 0:
        return 1
    if B == 1:
        return A % C
    n = B // 2
    m = B % 2
    temp = solve(A, n)
    if m == 0:
        return (temp * temp) % C
    else:
        return (temp * temp * A) % C

print(solve(A, B) % C)
