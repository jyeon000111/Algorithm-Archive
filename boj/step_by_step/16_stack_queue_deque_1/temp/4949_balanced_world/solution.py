# 목표: (), [], 알파벳, 공백 섞인 문자열(.으로 끝남)을 입력받아 괄호가 짝이 맞는지 판단
# 입력의 종료 조건: . 하나 입력
p_pair_dict = {')': '(', ']': '['}

while True:
    string = input()
    if string == '.':
        break  # 입력 종료

    stack = []  # 여는 괄호 담을 스택
    is_vps = True   # 짝이 맞다고 가정

    for char in string:  # 글자 하나씩 꺼내기
        if char == '(' or char == '[':  # 여는 괄호는 무조건 스택에 push
            stack.append(char)
        if char == ')' or char == ']':  # 닫는 괄호인 경우
            if not stack:  # 스택이 비어있으면
                is_vps = False  # 짝이 맞지 않다고 판단하고, 반복문 종료
                break
            else:  # 스택이 비어있지 않고
                if stack[-1] == p_pair_dict[char]:  # 짝이 맞으면, 스택에서 pop
                    stack.pop()
                else:  # 짝이 맞지 않으면, 반복문 종료
                    is_vps = False

    # 반복문 다 돌았는데, 스택에 괄호가 남았으면 false
    if stack:
        is_vps = False

    # 스택이 비었으면 균형 잡힌 것
    if is_vps:
        print('yes')
    else:
        print('no')
