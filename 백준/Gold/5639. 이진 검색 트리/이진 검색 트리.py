import sys
sys.setrecursionlimit(10000)

preorder = []
while True:
    word = sys.stdin.readline().strip()
    if word == "":
        break
    preorder.append(int(word))

answer = []
def build(start, end):
    if start > end:
        return

    root = preorder[start]
    idx = start + 1
    while idx <= end and preorder[idx] < root:
        idx += 1

    build(start + 1, idx - 1)
    build(idx, end)
    answer.append(root)

build(0, len(preorder) - 1)
for ans in answer:
    print(ans)