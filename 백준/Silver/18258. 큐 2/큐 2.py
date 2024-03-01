import sys
from collections import deque

#push X: 정수 X를 큐에 넣는 연산이다.
#pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#size: 큐에 들어있는 정수의 개수를 출력한다.
#empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
#front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

a = int(sys.stdin.readline())
blist = deque()
for _ in range(a):
    alist = sys.stdin.readline().split()
    if alist[0] == "push":
        blist.append(alist[1])
    elif alist[0] == "pop":
        if len(blist) > 0:
            print(blist.popleft())
        else:
            print("-1")
    elif alist[0] == "size":
        print(len(blist))
    elif alist[0] == "empty":
        if len(blist) == 0:
            print("1")
        else:
            print("0")
    elif alist[0] == "front":
        if len(blist) == 0:
            print("-1")
        else:
            print(blist[0])
    else:
        if len(blist) == 0:
            print("-1")
        else:
            print(blist[-1])
