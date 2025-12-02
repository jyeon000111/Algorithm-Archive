import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: 나무의 기둥의 길이와 가장 긴 가지의 길이 구하기
# - 기가 노드: 루트 노드에서 순회를 시작했을 때, 처음으로 자식 노드가 2개 이상인 노드
#   - 리프노드가 1개인 경우, 리프노드 = 기가노드
# 기둥의 길이: 루트 노드에서 기가 노드까지 간선들의 길이의 합!
# 가지의 길이: 기가 노드에서 리프 노드까지의 길이


# 트리 순회: 루트노드에서 출발. BFS 탐색
# 1. 기가 노드 찾기. (자식 노드 개수 처음으로 2개 이상인 경우)
# 2. 기가노드부터 모든 리프노드까지의 길이를 구하며 최댓값 갱신
# 그래프 - 인접 리스트(양방향)으로 저장  (주어지는 정보로는 뭐가 부모 노드인지 모름)
# visited로 무한 루프 방지

from collections import deque

def bfs(root_node):
    '''
    루트 노드를 인자로 받아,
    기가 노드를 찾아 기둥의 길이를 구하고,
    리프 노드를 찾아 가장 긴 가지의 길이를 갱신하는 함수입니다.
    '''
    global giga_node, giga_length, max_length

    dq = deque([(root_node, 0)])  # (노드 번호, 루트로부터의 길이)

    while dq:
        now, now_len = dq.popleft()

        # 아직 기가노드를 찾지 못한 경우
        if giga_node == -1:
            # 루트노드고, 인접노드가 2개 이상이면 기가노드
            # 루트노드가 아니고, 인접노드가 3개 이상이면 기가노드
            if (now == root_node and len(tree[now]) >= 2) or (now != root_node and len(tree[now]) >= 3):
                giga_node = now
                giga_length = now_len  # 기둥의 길이

        # 리프노드 : 자식 노드 0개
        if (now == root_node and len(tree[now]) == 0) or (now != root_node and len(tree[now]) == 1):
            # 1. 기가노드 못 찾은 경우
            if giga_node == -1:
                giga_length = now_len
                branch_len = 0
                max_length = max(branch_len, max_length)
            # 2. 기가 노드 찾은 경우
            else:
                branch_len = now_len - giga_length
                max_length = max(branch_len, max_length)

        # 너비 우선 탐색
        for next, next_len in tree[now]:
            if visited[next]:
                continue
            visited[next] = 1
            dq.append((next, now_len + next_len))







N, R = map(int, input().split())  # N은 노드(1~N번)의 개수, R은 루트 노드의 번호
# 간선 N-1 개의 정보 제공

tree = [[] for _ in range(N+1)]  # 1~N번 인덱스까지 사용, (인접 노드, 간선 길이) 저장

for _ in range(N-1):
    a, b, d = map(int, input().split())  # a번 노드와 b번 노드를 연결하는 간선의 길이 d
    tree[a].append((b, d))  # 양방향으로 저장
    tree[b].append((a, d))


max_length = -1  # 가지 길이의 최댓값
giga_node = -1  # 기가 노드 번호
giga_length = -1  # 루트-기가 길이
visited = [0] * (N+1)
visited[R] = 1  # 루트노드 방문 표시

bfs(R)  # 루트노드부터 전위 순회

print(giga_length, max_length)