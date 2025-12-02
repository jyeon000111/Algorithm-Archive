# 목표: 문자열에서 단어만 뒤집어서 출력
# 단어는 공백으로 구분. <> 사이의 단어는 그대로 출력.
# ' ' 또는 '<' '>' 문자 기준으로 stack 쌓기 -> 단어 출력 후, pop

S = input()  # 문자열 전체 입력받기
stack = []

for char in S:  # 한글자씩 탐색
    if char == '<':
        print(''.join(stack[::-1]), end='')
        stack = ['<']
    elif char == '>':
        print(''.join(stack), end='')
        print('>', end='')
        stack = []
    # 공백을 만나면 이전 단어 거꾸로 출력 (단, stack[0] != '<')
    elif char == ' ' and stack[0] != '<':
        print(''.join(stack[::-1]), end='')
        print(' ', end='')
        stack = []
    else:
        stack.append(char)
print(''.join(stack[::-1]))