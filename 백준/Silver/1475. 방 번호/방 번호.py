import sys

number = int(sys.stdin.readline())
counts = [0] * 10  

while number > 0:
    digit = number % 10
    counts[digit] += 1
    number //= 10

counts[6] = (counts[6] + counts[9] + 1) // 2  
counts[9] = 0  

print(max(counts))
