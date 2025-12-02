import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

def calculate(tokens):
    '''
    문자열로 이루어진 수식 리스트를 인자로 받아,
    왼쪽부터 순서대로 계산한 결과값을
    반환하는 함수입니다.
    (연산자는 +, -, *)
    '''
    stack = []
    for token in tokens:
        if token == '#':
            continue
        elif len(stack) == 2:
            oper = stack.pop()
            num1 = int(stack.pop())
            num2 = int(token)
            if oper == '+':
                result = num1 + num2
            elif oper == '-':
                result = num1 - num2
            else:
                result = num1 * num2
            stack.append(result)
        elif len(stack) < 2:
            stack.append(token)
    return stack[0]

def backtrack(cnt, tokens):
    '''
    고려한 연산자(괄호 넣을 수 있는 자리) 수와, 수식을 인자로 받아
    괄호를 추가할지 말지 정하고, 다음 자리로 넘기는 백트래킹 함수입니다.
    괄호를 추가하면, 양 옆 숫자를 #으로 바꾸고 계산한 결과를 연산자 자리에 입력합니다.
    '''
    if cnt == oper_cnt:
        temp_result = calculate(tokens)
        if not max_result:
            max_result.append(temp_result)
        elif max_result[0] < temp_result:
            max_result[0] = temp_result
        return

    # 고려할 연산자의 인덱스
    oper_idx = cnt * 2 + 1
    # 1. 괄호를 넣는 경우
    if tokens[oper_idx - 1] != '#':  # 이전 자리가 괄호가 아니어야 함
        num1 = int(tokens[oper_idx - 1])
        num2 = int(tokens[oper_idx + 1])
        oper = tokens[oper_idx]
        if oper == '+':
            result = num1 + num2
        elif oper == '-':
            result = num1 - num2
        else:
            result = num1 * num2
        new_tokens = tokens[:]
        new_tokens[oper_idx - 1] = '#'
        new_tokens[oper_idx] = result
        new_tokens[oper_idx + 1] = '#'
        # 다음 자리로 넘어가기 (한 자리 건너뛰기)
        backtrack(cnt+1, new_tokens)

    # 2. 괄호를 넣지 않고 넘어가는 경우
    backtrack(cnt+1, tokens)



# 목표: 연산자 하나만 포함하는 괄호를 추가하여 만들 수 있는 결과의 최댓값 구하기 (괄호 개수는 0개부터 무제한. 중첩된 괄호 사용 불가)
# - 계산은 우선순위 없이 왼쪽부터 순서대로
N = int(input())  # 수식의 길이
given_tokens = list(input())  # 수식 (포함된 정수는 0 이상 9 이하 한자리 수)
if N == 1:  # 수식의 길이가 1일 때, 예외 처리
    max_result = [int(given_tokens[0])]
else:
    oper_cnt = N // 2  # 괄호 넣을 수 있는 자리 수 = 연산자 수
    max_result = []
    backtrack(0, given_tokens)

print(*max_result)