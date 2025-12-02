N = int(input())  # 명령의 수
stack = []
def do_command(n):
    '''명령 번호를 문자열로 입력받아
    명령을 처리하는 함수입니다.
    '''
    if len(n) > 1:  # (1, x) 튜플 입력 시
        num = tuple(map(int, n.split()))
        stack.append(num[1])  # 정수 x를 스택에 push
    else:
        num = int(n)
        if num == 2:
            # 스택에 정수가 있다면, 맨 위의 정수를 pop해서 출력
            if stack:
                print(stack.pop())
            # 없다면, -1 출력
            else:
                print(-1)
        elif num == 3:
            # 스택에 들어있는 개수 출력
            print(len(stack))
        elif num == 4:
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

for _ in range(N):
    data = input()
    do_command(data)