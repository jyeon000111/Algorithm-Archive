# 목표: 괄호 문자열이 올바른지 판단해서 'YES', 'NO' 출력

T = int(input())
for _ in range(T):
    ps = input()
    if len(ps) % 2 == 1:  # 문자열 길이가 홀수이면, 유효하지 않다.
        print('NO')
        continue
    stack = []
    is_vps = True  # 유효하다고 가정
    for p in ps:
        if p == '(':
            stack.append(p)
        elif stack:  # 닫는 괄호고, 스택에 여는 괄호가 있으면
            stack.pop()  # 하나를 제거한다.
        else:  # 닫는 괄호고, 스택이 비었으면
            is_vps = False # 유효하지 않다.
            break  # for p 종료
    # 반복문 다 돌고, stack에 값이 남았으면 유효하지 않다.
    if stack:
        is_vps = False
    # stack에 값이 없으면 유효하다.

    if is_vps:
        print('YES')
    else:
        print('NO')