# import sys
# # --- 파일 입출력 설정 ---
# # 입력 파일 경로
# sys.stdin = open("input.txt", "r")
# --------------------

# 목표: 나무의 기둥의 길이와 가장 긴 가지의 길이 구하기
# - 기가 노드: 루트 노드에서 순회를 시작했을 때, 처음으로 자식 노드가 2개 이상인 노드
#   - 리프노드가 1개인 경우, 리프노드 = 기가노드
# 기둥의 길이: 루트 노드에서 기가 노드까지 간선들의 길이의 합!
# 가지의 길이: 기가 노드에서 리프 노드까지의 길이




# 그래프 - 인접 리스트(양방향)으로 저장  (주어지는 정보로는 뭐가 부모 노드인지 모름)
# 0. 자식 노드 수 미리 구해서 배열에 넣어놓기.
# 1. 기가 노드 찾기. (자식 노드 개수 처음으로 2개 이상인 경우)
# 2. 기가 노드에서 BFS 출발 -> 기가노드-리프노드 길이의 최댓값 갱신
from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    global max_branch_len

    dq = deque([(start, 0)])  # (현재 노드, 기가노드로부터의 이동거리)

    while dq:
        now, now_len = dq.popleft()

        if children_cnt_list[now] == 0:  # 리프노드
            max_branch_len = max(now_len, max_branch_len)

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

children_cnt_list = [-1] * (N+1)  # 배열에 자식 수 저장 (루트노드 아니면 인접노드 수에서 부모노드 1개만 제외하면 됨)
for idx in range(1, N+1):
    children_cnt_list[idx] = len(tree[idx]) - 1

children_cnt_list[R] += 1  # 루트노드는 부모노드 없음

# 1. 기가노드 찾기
parent = R  # 루트노드에서 시작
visited = [0] * (N+1)
giga_length = 0
while True:
    visited[parent] = 1

    if children_cnt_list[parent] >= 2 or children_cnt_list[parent] == 0:
        giga_node = parent
        break
    # 자식 무조건 1명
    for child, len in tree[parent]:
        if visited[child]:
            continue
        giga_length += len
        parent = child

# 2. 기가 노드에서 BFS 출발
max_branch_len = -1

bfs(giga_node)

print(giga_length, max_branch_len)
