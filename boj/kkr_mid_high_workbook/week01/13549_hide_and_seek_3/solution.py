# import sys
# # --- 파일 입출력 설정 ---
# # 입력 파일 경로
# sys.stdin = open("input.txt", "r")
# --------------------
from collections import deque

N, K = map(int, input().split())

def bfs(start, target):
    '''시작 위치와 목표 위치를 인자로 받아
    목표 위치까지의 최소 시간을 반환하는 함수'''

    dq = deque([(0, start)])  # (현재까지 소요 시간, 현재 위치)
    visited = {start,}  # 중복 방문 방지


    while dq:
        time, now = dq.popleft()
        if now == target:
            return time 
        if (now - 1) not in visited:
            dq.append((time + 1, now - 1))
            visited.add(now - 1)
        if (now + 1) not in visited:
            dq.append((time + 1, now + 1))
            visited.add(now + 1)
        if (now < target) and ((now * 2) not in visited):
            dq.append((time, now * 2))
            visited.add(now * 2)



print(bfs(N, K))