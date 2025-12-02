import sys
sys.stdin = open("input.txt", "r")
# 목표: 0과 1로 이루어진 2차원 배열을 재귀적으로 4등분하면서 압축 표현 => 쿼드 트리 출력

def quad_tree(cur_r, cur_c, cur_size):
    '''
    좌상단 기준점의 좌표, 한 변의 길이를 인자로 받아
    모두 동일한 숫자로 이루어져있으면, 결과리스트에 해당 숫자를 추가한다.
    다른 숫자가 섞여있으면, 4등분해서 재귀호출한다.
    괄호로 재귀 깊이를 구분한다.
    '''
    cur_num = arr[cur_r][cur_c]  # 좌상단 기준점 숫자

    if cur_size == 1:
        result.append(cur_num)
        return

    for dr in range(cur_size):
        for dc in range(cur_size):
            if arr[cur_r + dr][cur_c + dc] != cur_num:  # 다른 숫자 섞여있으면
                result.append('(')
                # 4등분해서 재귀호출
                next_size = cur_size // 2
                quad_tree(cur_r, cur_c, next_size)
                quad_tree(cur_r, cur_c + next_size, next_size)
                quad_tree(cur_r + next_size, cur_c, next_size)
                quad_tree(cur_r + next_size, cur_c + next_size, next_size)
                result.append(')')
                return

    result.append(cur_num)  # 모두 동일한 숫자인 경우, 해당 숫자 결과에 추가하고 종료




N = int(input())
arr = [list(input()) for _ in range(N)]

result = []
quad_tree(0, 0, N)

print(''.join(result))