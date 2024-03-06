def largest_rectangle(histogram):
    stack = []
    max_area = 0

    for i, h in enumerate(histogram):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))

    for index, height in stack:
        max_area = max(max_area, height * (len(histogram) - index))

    return max_area



while True:
    alist = list(map(int, input().split()))
    alist.pop(0)

    if len(alist) == 0:
        break
    print(largest_rectangle(alist))
