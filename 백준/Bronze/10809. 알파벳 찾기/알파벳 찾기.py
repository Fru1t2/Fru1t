word = input()

alphabet_list = [chr(i) for i in range(97, 123)]
output = []

for i in range(len(alphabet_list)):
    for j in range(len(word)):
        if alphabet_list[i] in word:
            if alphabet_list[i] in output:
                continue

            if alphabet_list[i] == word[j]:
                print(j, end=' ')
                output.append(alphabet_list[i])

    if alphabet_list[i] not in word:
        print("-1", end=' ')
