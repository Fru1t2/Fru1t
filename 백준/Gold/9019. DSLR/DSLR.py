from collections import deque
import sys

def D(n): return (2 * n) % 10000
def S(n): return 9999 if n == 0 else n - 1
def L(n): return (n % 1000) * 10 + (n // 1000)
def R(n): return (n % 10) * 1000 + (n // 10)
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())

    visited = [False] * 10000
    from_list = [-1] * 10000
    how = [''] * 10000

    queue = deque()
    queue.append(A)
    visited[A] = True

    while queue:
        now = queue.popleft()
        for op, next_num in zip("DSLR", [D(now), S(now), L(now), R(now)]):
            if not visited[next_num]:
                visited[next_num] = True
                from_list[next_num] = now
                how[next_num] = op
                queue.append(next_num)
                if next_num == B:
                    break
    res = []
    cur = B
    while cur != A:
        res.append(how[cur])
        cur = from_list[cur]

    print(''.join(reversed(res)))
