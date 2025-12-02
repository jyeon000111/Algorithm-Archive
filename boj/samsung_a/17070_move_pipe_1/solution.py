import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------
from collections import deque

def bfs(start_headi, start_headj, start_reari, start_rearj):
    '''
    시작 시점의 머리쪽 좌표, 꼬리쪽 좌표를 인자로 받아
    이동가능한 모든 위치를 너비우선탐색합니다.
    머리가 (N-1, N-1)에 도달하면 카운트합니다.
    '''
    global ans_cnt

    dq = deque([(start_headi, start_headj, start_reari, start_rearj)])

    while dq:
        hi, hj, ri, rj = dq.popleft()
        # 머리가 (N-1, N-1) 도착하면 카운트
        if hi == N-1 and hj == N-1:
            ans_cnt += 1

        # 0. 세 가지 방향 모두 대각선 이동 가능. 대각선으로 밀었을 때, 인덱스 밖으로 나가거나, 벽이 없는지 체크
        # - 머리 기준 오른쪽, 대각선 아래, 아래쪽 이 비어있는지 체크
        can_move_diagnose = False
        if hi + 1 <= N - 1 and hj + 1 <= N - 1:
            can_move_diagnose = True
        for di, dj in [(0, 1), (1, 1), (1, 0)]:
            nhi, nhj = hi + di, hj + dj
            if 0 <= nhi < N and 0 <= nhj < N:
                if arr[nhi][nhj] == 1:
                    can_move_diagnose = False
                    break

        # 1. 가로 방향일 때 (머리와 꼬리가 같은 행)
        if hi == ri:
            # 1) 가로 이동
            if (hj+1 <= N-1) and (arr[hi][hj+1] == 0):
                dq.append((hi, hj+1, ri, rj+1))
            # 2) 대각선 이동
            if can_move_diagnose:
                dq.append((hi+1, hj+1, ri, rj+1))


        # 2. 세로 방향일 때 (머리와 꼬리가 같은 열)
        elif hj == rj:
            # 1) 세로 이동
            if (hi+1 <= N-1) and (arr[hi+1][hj] == 0):
                dq.append((hi+1, hj, ri+1, rj))

            # 2) 대각선 이동
            if can_move_diagnose:
                dq.append((hi+1, hj+1, ri+1, rj))

        # 3. 대각선 방향일 때 (위 두 가지 경우 제외)
        else:
            # 1) 가로 이동
            if (hj+1 <= N-1) and (arr[hi][hj+1] == 0):
                dq.append((hi, hj+1, ri+1, rj+1))

            # 2) 세로 이동
            if (hi+1 <= N-1) and (arr[hi+1][hj] == 0):
                dq.append((hi+1, hj, ri+1, rj+1))

            # 3) 대각선 이동
            if can_move_diagnose:
                dq.append((hi+1, hj+1, ri+1, rj+1))



N = int(input())  # 집의 크기 N * N
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)
ans_cnt = 0
bfs(0, 1, 0, 0)
print(ans_cnt)