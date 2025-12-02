import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: n개의 별들을 모두 이어 별자리를 만든다. 별자리를 만드는 최소 비용(거리) 구하기
# MST - prim
# 정점을 기준으로 가까운 곳부터 이동
from heapq import heappop, heappush  # 우선순위 큐로 작은 거리부터 이동
from math import sqrt

def mst():
    MST = [0] * n

    pq = [(0, 0)]  # (거리의 제곱, 별 인덱스)  - 0번 별부터 시작

    min_dist = 0  # 최소 거리 초기화

    star_cnt = 0  # 연결한 별의 개수


    while pq:
        now_dist, now_idx = heappop(pq)  # 가까운 별부터 꺼내서 이동
        if MST[now_idx]:
            continue
        MST[now_idx] = 1
        star_cnt += 1
        min_dist += sqrt(now_dist)  # 제곱근으로 제대로 된 거리를 구하여 더하기

        if star_cnt == n:  # n개의 별을 다 연결했으면 최소 거리 반환하고 종료! 
            return min_dist

        for next_idx in range(n):
            if next_idx == now_idx:  # 현재 정점이면 패스
                continue
            if MST[next_idx]:  # 연결한 정점이면 패스
                continue
            # 거리의 제곱! 
            next_dist = (stars[now_idx][0] - stars[next_idx][0]) ** 2 + (stars[now_idx][1] - stars[next_idx][1]) ** 2
            heappush(pq, (next_dist, next_idx))
    
    
    


n = int(input())  # 별의 개수
stars = []  # 별의 x, y 좌표
for _ in range(n):
    stars.append(tuple(map(float, input().split())))

ans = mst()
print(ans)
