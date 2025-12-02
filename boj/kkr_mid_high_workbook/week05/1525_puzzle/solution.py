# import sys
# # --- 파일 입출력 설정 ---
# # 입력 파일 경로
# sys.stdin = open("input.txt", "r")
# --------------------

# 목표: 숫자 퍼즐을 순서대로 정리하는 최소 이동 횟수 구하기 (이동 불가능한 경우 -1 출력)
# - 0은 빈 칸. 숫자를 상하좌우 인접한 빈칸으로 이동시킬 수 있음. 

# [ 아이디어 ]
# 최단경로 => BFS
# 3*3 퍼즐 상태는 2차원 배열이 아닌 문자열로 저장
# - 왜? 메모리 효율 / 단순한 좌표 관리 / set에 방문 기록하기 좋음.
# - 이동 가능한 인접칸의 인덱스 -> 배열에 미리 저장해두기
# 정답상태 '123456780' 
# 중복 방문, 무한 루프 방지 => set에 방문 기록


import sys
from collections import deque
input = sys.stdin.readline

# 정답 상태 정의
ANSWER = '123456780'

# 이동 가능한 인덱스 미리 구해두기 
MOVE_IDX = [
    (1, 3),
    (0, 2, 4),
    (1, 5),
    (0, 4, 6),
    (1, 3, 5, 7),
    (2, 4, 8),
    (3, 7),
    (4, 6, 8),
    (5, 7),
    ]


def bfs(initial):
    '''
    9자리 퍼즐 문자열을 인자로 받아, 
    빈칸 0을 이동가능한 인덱스 위치로 이동한다.
    BFS를 진행하면서 정답상태와 동일해지면 그때의 이동횟수를 반환한다.
    BFS 다 돌려도 정답상태에 도달하지 못했다면, -1을 반환한다.
    '''
    visited = {initial}  # 무한루프 방지, 초기 상태 기록
    
    
    dq = deque([(initial, 0)])  # (문자열, 이동횟수)
    
    while dq:
        cur_str, cur_move = dq.popleft()
        
        if cur_str == ANSWER:  # 정답상태 도달한 경우
            return cur_move
        
        blank_idx = cur_str.index('0')  # 빈칸 인덱스
        
        for idx_to_change in MOVE_IDX[blank_idx]:
            temp_list = list(cur_str)
            temp_list[blank_idx], temp_list[idx_to_change] = temp_list[idx_to_change], temp_list[blank_idx]
            next_str = ''.join(temp_list)
            if next_str in visited:
                continue
            else:
                visited.add(next_str)
                dq.append((next_str, cur_move + 1))
                
            
    return -1 





initial_str = ''  # 문자열 1줄로 평탄화
for _ in range(3):
    initial_str += ''.join(input().split())



# 패리티 검사 : 역전 개수(빈칸 제외)가 홀수면 풀 수 없음!
inversion_cnt = 0
initial_int_list = list(map(int, initial_str))  # 미리 정수 리스트로 변환
for i1 in range(9):
    for i2 in range(i1+1, 9):
        c1 = initial_int_list[i1]
        c2 = initial_int_list[i2]
        if c1 == 0 or c2 == 0:
            continue
        if c1 > c2:
            inversion_cnt += 1
if inversion_cnt % 2 != 0:
    print(-1)
else:
    ans = bfs(initial_str)
    print(ans)