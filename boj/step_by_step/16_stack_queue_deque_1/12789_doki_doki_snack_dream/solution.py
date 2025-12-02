N = int(input())  # 학생의 수
order_list = list(map(int, input().split()))[::-1]  # 1~N 번호표 순서: 뒤에서부터 꺼내고 pop해서 하나씩 지우기 위해 역순으로 뒤집기

# 순서가 아닌 사람을 스택에 쌓았다가,
# 다시 순서대로 들어갈 수 있는 라인으로 보냈을 때 모두 통과하면, 간식 받을 수 있음

# 목표: 간식을 받을 수 있으면 'Nice', 그렇지 않다면 'Sad' 출력
get_snack = True  # 간식을 받을 수 있다고 가정

current_snack_num = 1  # 이번에 간식 받을 사람 번호
stack = []  # 자기 순서 아닌 사람 담는 스택

while order_list:  # 번호표가 모두 처리될 때까지 반복
    num = order_list[-1]

    if num == current_snack_num:  # 간식 받을 순서 맞으면 통과
        order_list.pop()  # 처리된 번호표 제거
        current_snack_num += 1
    else:  # 간식 받을 순서 아닌 경우
        # 스택에 내림차순으로 쌓여야 한다.
        # 스택이 비었으면 push
        if not stack:
            stack.append(num)
            order_list.pop()

        # 스택에 값이 있을 때
        else:
            # 스택의 마지막 값보다 현재 번호표가 작을 때만 push
            if stack[-1] > num:
                stack.append(num)
                order_list.pop()
            # 스택의 마지막 값이 더 작으면, current_snack_num 인지 체크
            else:
                if stack[-1] == current_snack_num:
                    stack.pop()  # 맞으면 해당 번호 제거하고 현재 간식 번호 1 증가
                    current_snack_num += 1

                else:  # -> 아니면 간식 못 받음.. 반복 종료!
                    get_snack = False
                    break  # for num 종료

if get_snack:
    print('Nice')
else:
    print('Sad')