import sys

N, M = map(int, sys.stdin.readline().split())
text = list(sys.stdin.readline().strip())

first, last = 0, N-1
while first <= last and M > 0:
    if text[first] > text[last]:
        last -= 1
    elif text[first] < text[last]:
      text[first], text[last] = text[last], text[first]
      first += 1
      last -=1
      M -= 1
    elif text[first] == text[last] and text[first] == 'P':
        first += 1
    elif text[first] == text[last] and text[first] == 'C':
        last -= 1

count_p = 0
answer = 0
for i in range(N):
    if text[i] == 'P':
        count_p += 1
    elif text[i] == 'C':
        answer += (count_p * (count_p - 1)) // 2

print(answer)
