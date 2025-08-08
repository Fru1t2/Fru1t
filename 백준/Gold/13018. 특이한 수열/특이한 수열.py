import sys

def solve():
    input = sys.stdin.readline
    n, k = map(int, input().split())

    if k > n - 1:
        print("Impossible")
        return

    A = list(range(n + 1))
    d = (n - 1) - k
    t2 = d // 2
    for j in range(t2):
        i = 2 + 2 * j
        if i + 1 <= n:
            A[i], A[i + 1] = A[i + 1], A[i]

    if d % 2 == 1:
        r = 2 + 2 * t2
        if r > n:
            r = 2
        A[1], A[r] = A[r], A[1]

    print(*A[1:])

if __name__ == "__main__":
    solve()
