arr = ["c=","c-","dz=","d-","lj","nj","s=","z="]
word = input()
output = 0

for a in arr:
    word = word.replace(a, "0")

print(len(word))