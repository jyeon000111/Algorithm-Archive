# import sys
# # --- 파일 입출력 설정 ---
# # 입력 파일 경로
# sys.stdin = open("input.txt", "r")
# # 출력 파일 경로
# sys.stdout = open("output.txt", "w")
# # --------------------

# 목표:
# 1. 수빈이가 동생 위치로 이동하는 가장 빠른 시간이 몇 초 후인지 출력
# 2. 가장 빠른 시간으로 찾는 방법이 몇 가지인지 출력

# 이동 규칙 : X-1 / X+1 / 2*X 로 이동
# => BFS
from collections import deque

def bfs(start, target):
    global min_time, ans_cnt
    dq = deque([(start, 0)])  # (현재 위치, 현재 위치까지 소요 시간)

    while dq:
        # print(dq)
        now, time = dq.popleft()
        if time >= min_time:
            return
        next1 = now - 1
        next2 = now + 1
        next3 = now * 2
        if next1 == target or next2 == target or next3 == target:  # 다음 숫자가 target이면 다음이 최소시간
            # 더 이상 인큐하거나, visited에 저장할 필요 없음.
            min_time = time + 1
            ans_cnt += 1
        else:  # 인큐, visited 에 저장
            if next1 not in visited:
                visited.add(next1)
                dq.append((next1, time + 1))
            if next2 not in visited:
                visited.add(next2)
                dq.append((next2, time + 1))
            if next3 not in visited:
                visited.add(next3)
                dq.append((next3, time + 1))




N, K = map(int, input().split())  # 수빈이가 있는 위치 N, 동생이 있는 위치 K

visited = set()  # 도착한 숫자 중복 방문하지 않도록 셋에 저장

min_time = float('inf')  # 최소 시간 초기화
ans_cnt = 0  # 최소 시간 찾는 경우의 수

bfs(N, K)
print(min_time)
print(ans_cnt)