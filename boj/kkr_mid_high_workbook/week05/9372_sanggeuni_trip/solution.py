# import sys
# # --- 파일 입출력 설정 ---
# # 입력 파일 경로
# sys.stdin = open("input.txt", "r")
# --------------------

# 목표: 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수
# - 한 국가에서 다른 국가 이동할 때, 다른 국가 거쳐가거나 재방문해도 됨.
# - 가중치 없는 양방향 그래프!



T = int(input())  # 테스트케이스 수
for _ in range(T):
    N, M = map(int, input().split())  # N은 국가 수(1~N번), M은 비행기 수
    for _ in range(M):
        input()

    # 모든 정점을 연결하는 최소 간선 수는 N-1 개
    print(N-1)

