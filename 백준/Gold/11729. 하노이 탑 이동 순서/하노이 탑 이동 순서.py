import sys

def Hanoi(n, start, temp, final):
    if n == 1:
        return print(start, final)
    Hanoi(n - 1, start, final, temp)
    print(start, final)
    Hanoi(n - 1, temp, start, final)


N = int(sys.stdin.readline())
print(2**N-1)
Hanoi(N, 1, 2, 3)