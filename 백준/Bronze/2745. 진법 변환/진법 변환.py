dic = {}
output = 0
start_char = ord('A')
for i in range(26):
    char = chr(start_char + i)
    dic[char] = 10 + i

N, B = input().split()
B = int(B)

for i in range(len(N)):
    if N[len(N)-i-1] not in dic.keys():
        a = int(N[len(N)-i-1])
        output += a*(B**i)
    if N[len(N)-i-1] in dic.keys():
        b = dic[N[len(N)-i-1]]
        output += b*(B**i)

print(output)