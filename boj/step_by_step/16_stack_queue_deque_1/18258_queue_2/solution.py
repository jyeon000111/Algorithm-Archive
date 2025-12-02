import sys
input = sys.stdin.readline
from collections import deque

N = int(input())  # 명령의 수
dq = deque()  # 덱 자료구조 활용 (앞에 있는 데이터를 빼야 하므로)

for _ in range(N):
    tokens = input().split()
    if tokens[0] == 'push':
        dq.append(tokens[1])
    elif tokens[0] == 'pop':
        if dq:  # 스택에 값이 있으면
            print(dq.popleft())
        else:
            print(-1)
    elif tokens[0] == 'size':
        print(len(dq))
    elif tokens[0] == 'empty':
        if dq:  # 스택에 값이 있으면
            print(0)
        else:
            print(1)
    elif tokens[0] == 'front':
        if dq:  # 스택에 값이 있으면
            print(dq[0])
        else:
            print(-1)
    else:  # back 입력
        if dq:
            print(dq[-1])
        else:
            print(-1)