N = int(input()) # 수의 개수
numbers = list(map(int, input().split()))  # N개의 순서가 정해진 숫자 리스트
operator_cnt = list(map(int, input().split()))  # +, -, *, / 총 N-1개의 연산자

# 목표: 첫째 줄에 만들 수 있는 식의 결과의 최댓값, 둘째 줄에 최솟값 출력

# 1. 숫자 리스트, 연산자 리스트를 인자로 받아 계산 결과 도출하는 함수 만들기
# - 계산 방법: 우선 순위 무시하고 앞에서부터 계산.
def calculate(num_list, oper_list):
    '''숫자 리스트(길이 N), 연산자 리스트(길이 N-1)를 인자로 받아 
    계산 결과를 반환하는 함수입니다.
    '''
    num1 = num_list[0]
    for idx in range(N-1): # 0~N-2 인덱스 순회
        num2 = num_list[idx + 1]
        oper = oper_list[idx]
        if oper == '+':
            num1 += num2
        elif oper == '-':
            num1 -= num2
        elif oper == '*':
            num1 *= num2
        else:
            if num1 < 0:
                num1 = -(-num1 // num2)
            else:
                num1 //= num2

    return num1


# 2. 백트래킹으로 연산자 리스트 만들기. 깊이 끝에 도달하면 계산 결과 구하고 최댓값, 최솟값 갱신
# - 백트래킹 알고리즘 : 불필요한 탐색 차단
max_result = []  # 최댓값 담을 리스트
min_result = []  # 최솟값 담을 리스트
operators = ['+', '-', '*', '/']

def solve(oper_list):
    '''연산자를 담을 리스트를 인자로 받아
    N-1 길이가 될 때까지 연산자를 채우고,
    계산 결과를 구하여 최댓값, 최솟값을 갱신하는
    함수입니다.
    '''
    if len(oper_list) == (N-1):  # 모든 연산자를 담으면 종료
        current_result = calculate(numbers, oper_list)
        # 최댓값 최솟값 담을 리스트가 비어 있으면 현재값 추가
        if not max_result:
            max_result.append(current_result)
            min_result.append(current_result)
        else:  # 비어 있지 않으면 비교해서 갱신
            if max_result[0] < current_result:
                max_result[0] = current_result
            if min_result[0] > current_result:
                min_result[0] = current_result
        return
    
    for i in range(4):  # 인덱스 순회
        # 해당 인덱스의 연산자가 없으면 continue
        if not operator_cnt[i]:
            continue
        # 해당 인덱스의 연산자 있으면 
        # 1) operator_cnt[i] 값 1 감소
        # 2) oper_list에 추가
        else:
            operator_cnt[i] -= 1
            oper_list.append(operators[i])

            # 다음 재귀로 넘어가기
            solve(oper_list)

            # 돌아와서 원상복구
            operator_cnt[i] += 1
            oper_list.pop()

solve([])
print(*max_result)
print(*min_result)


