import sys

def kantor(mlist):
    if len(mlist) == 1:
        return mlist
    else:
        alist = []
        blist = []
        clist = []
        for i in range((len(mlist)//3), 2*(len(mlist))//3):
            clist.append(" ")
        for j in range((len(mlist)//3)):
            alist.append(mlist[j])
        for k in range(2*(len(mlist)//3),len(mlist)):
            blist.append(mlist[k])
        return kantor(alist) + clist + kantor(blist)

N = []
while True:
    line = sys.stdin.readline().strip()  # 개행 문자 제거
    if not line:  # 파일의 끝에 도달하면 빈 문자열이 반환됨
        break
    num = int(line)  # 정수로 변환
    N.append(num)

for i in N:
    alist = []
    for _ in range(3**i):
        alist.append("-")

    print(''.join(kantor(alist)))
