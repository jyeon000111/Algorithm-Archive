# 시간초과 -> sys.stdin.readline()으로 입력 받기
import sys

N = int(sys.stdin.readline())  # 명령의 수
stack = []

for _ in range(N):
    tokens = list(map(int, sys.stdin.readline().split()))  # 공백 기준으로 나눈 정수를 리스트에 담기

    if len(tokens) > 1:  # [1, x] 튜플 입력 시
        stack.append(tokens[1])  # 정수 x를 스택에 push
    else:
        if tokens[0] == 2:
            # 스택에 정수가 있다면, 맨 위의 정수를 pop해서 출력
            if stack:
                print(stack.pop())
            # 없다면, -1 출력
            else:
                print(-1)
        elif tokens[0] == 3:
            # 스택에 들어있는 개수 출력
            print(len(stack))
        elif tokens[0] == 4:
            # 비어있으면 1, 아니면 0 출력
            if stack:
                print(0)
            else:
                print(1)
        else:  # 5 입력
            # 스택에 정수 있다면 맨 위의 정수 출력
            if stack:
                print(stack[-1])
            else:  # 없다면 -1 출력
                print(-1)