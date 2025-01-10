import sys
from collections import deque

num_test = int(sys.stdin.readline())
for _ in range(num_test):
    switch = True
    command = deque(sys.stdin.readline().strip())
    num_case = int(sys.stdin.readline().strip())
    if num_case == 0:
        case = deque()
        sys.stdin.readline()
    else:
        case = deque(map(int, (sys.stdin.readline().strip())[1:-1].split(',')))

    for com in command:
        if com == "R":
            switch = not switch
        elif com == "D":
            if len(case) != 0:
                if switch:
                    case.popleft()
                else:
                    case.pop()
            else:
                print("error")
                break
    else:
        if switch:
            output = "[" + ",".join(map(str, case)) + "]"
        else:
            case.reverse()
            output = "[" + ",".join(map(str, case)) + "]"
        print(output)
