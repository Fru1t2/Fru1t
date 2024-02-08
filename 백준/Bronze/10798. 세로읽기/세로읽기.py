high = 0
arr = ""
words = [input() for i in range(5)]

for i in range(5):
    if len(words[i]) > high:
        high = len(words[i])

for j in range(high):
    for k in range(5):
        try:
            arr = arr + words[k][j]
        except IndexError:
            arr = arr + ""

print(arr)