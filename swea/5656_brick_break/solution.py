import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------
from copy import deepcopy
from collections import deque

def drop_ball(j, arr):
    '''
    BFS를 활용하여, 제거될 구슬을 목록에 담아 순서대로 처리한다.
    열 인덱스와 배열을 인자로 받아
    j열에 구슬을 떨어뜨렸을 때의 연쇄작용을
    배열에 표시한다.
    제거된 벽돌을 0으로 변경한다.
    '''

    # 벽돌이 깨지는 시작점 구하기
    # + 빈 열 처리 추가
    start_found = False
    for i in range(H):
        if arr[i][j] > 0:
            starti, startj = i, j
            val = arr[i][j]
            start_found = True
            break

    if not start_found:
        return arr

    arr[starti][startj] = 0
    dq = deque([(starti, startj, val)])

    while dq:
        nowi, nowj, val = dq.popleft()

        if val == 1:
            continue
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            for c in range(1, val):
                ni = nowi + di * c
                nj = nowj + dj * c
                if (0 <= ni < H) and (0 <= nj < W) and (arr[ni][nj] != 0):
                    nval = arr[ni][nj]
                    arr[ni][nj] = 0
                    dq.append((ni, nj, nval))

    return arr

def rearrange(arr):
    '''
    H*W 배열을 인자로 받아,
    모든 열의 숫자들을 사이에 0이 없게 밑으로 재배치한다.
    '''
    new_arr = [[0] * W for _ in range(H)]  # 재배치할 배열을 0으로 초기화
    stack = []  # 위에서부터 숫자를 찾아 push하고, pop해서 밑에서부터 숫자를 입력한다.
    for j in range(W):
        for i in range(H):
            if arr[i][j] == 0:
                continue
            stack.append(arr[i][j])
        ni = H-1
        while stack:
            new_arr[ni][j] = stack.pop()
            ni -= 1
    return new_arr


def backtrack(ball_cnt, arr):
    '''
    사용한 구슬의 개수, 현재 벽돌 배열을 인자로 받아,
    벽돌을 깨는 모든 경우의 수를 백트래킹으로 탐색한다.
    N개의 구슬을 사용하면, 남은 벽돌의 개수를 구하고,
    최소 개수를 갱신한다.
    '''
    global min_ans

    # 구슬이 남았는데, 벽돌이 없는 경우 처리..
    is_no_brick = True  # 벽돌 없다고 가정
    # 하나라도 찾으면 False 처리하고 반복문 종료
    for j_idx in range(W):
        if arr[H-1][j_idx] > 0:
            is_no_brick = False
            break
    if is_no_brick:
        min_ans = 0
        return

    if ball_cnt == N:
        remain_brick = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] > 0:
                    remain_brick += 1
        # print('디버깅1. 구슬 다 쓰고 남은 벽돌의 수:', remain_brick)
        if min_ans > remain_brick:
            min_ans = remain_brick
        return

    # 각 열의 맨 아래가 0이면 비어있는 열!
    for j in range(W):
        if arr[H-1][j] == 0:
            continue
        arr2 = deepcopy(arr)  # 초기화
        # j열에 구슬을 떨어뜨리는 경우의 연쇄작용을 함수로 분리한다.
        arr2 = drop_ball(j, arr2)
        # #------------ 디버깅2 ------------------
        # temp_brick = 0
        # for r in range(H):
        #     for c in range(W):
        #         if arr2[r][c] > 0:
        #             temp_brick += 1
        # print(f'디버깅2. {j}열에 {ball_cnt + 1}번째 구슬 떨어뜨린 후 남은 벽돌의 수:', temp_brick)
        # # -------------------------------------

        # 벽돌 사이의 빈 공간을 없애고, 벽돌을 밑으로 재배치한다.
        arr2 = rearrange(arr2)
        backtrack(ball_cnt + 1, arr2)  # 다음 구슬로 넘어가기



T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    map_arr = [list(map(int, input().split())) for _ in range(H)]
    # N은 구슬 개수, 벽돌 배열이 H * W 배열로 주어짐.
    # 목표: 구술 N개를 떨어뜨려 최대한 많은 벽돌을 제거할 때, 남은 벽돌의 개수 구하기
    # - 제거된 벽돌은 (벽돌에 적힌 숫자 -1)칸 만큼 같이 제거됨.(동시에)
    # - 빈 공간이 있을 경우, 벽돌은 밑으로 떨어지게 됨.
    # => N, W, H의 최대입력값이 크지 않으므로, 이중리스트로 구현해도 됨!
    # 완전 탐색, 백트래킹
    min_ans = H * W  # 최소 벽돌 개수 초기화

    backtrack(0, map_arr)
    print(f'#{tc} {min_ans}')