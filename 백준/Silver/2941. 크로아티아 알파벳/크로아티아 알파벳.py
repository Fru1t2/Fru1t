arr = ["c=","c-","dz=","d-","lj","nj","s=","z="]
word = input()
output = 0

for pattern in arr:
    count = word.count(pattern)  # 각 패턴의 출현 횟수를 센다
    output += count
    word = word.replace(pattern, "가")  # 해당 패턴을 모두 제거한다

while "가" in word:
    word = word.replace("가","")

output += len(word)

print(output)