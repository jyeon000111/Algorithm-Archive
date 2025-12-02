import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: 최소 스패닝 트리의 가중치 출력
# - 최소 스패닝 트리: 모든 정점들을 연결하는 그래프 중에서 가중치의 합이 최소인 트리
# MST - Kruskal 알고리즘 - 유니온 파인드
# - 가중치 기준으로 간선들을 정렬. 가중치가 낮은 간선부터 연결


def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_y == rep_x:
        return
    if ranks[rep_x] > ranks[rep_y]:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y
        if ranks[rep_x] == ranks[rep_y]:  # 랭크 동일할 때는 부모노드가 된 대표자 랭크 +1
            ranks[rep_y] += 1



V, E = map(int, input().split())  # 정점의 개수, 간선의 개수


edges = []  # (가중치, 시작점, 끝점)
for _ in range(E):
    start, end, w = map(int, input().split())
    edges.append((w, start, end))

edges.sort()  # 가중치 기준 오름차순 정렬

# 유니온파인드 세팅
parents = [num for num in range(V+1)]  # 1~V번
ranks = [0] * (V+1)

ans_weight = 0
cnt = 0
for weight, s, e in edges:  # 가중치 낮은 간선부터 고려
    if cnt == V - 1:  # 정점보다 1개 적은 간선이 사이클 없이 연결되었으면 신장트리 완성
        break
    # 연결되어 있으면 패스
    if find_set(s) == find_set(e):
        continue
    # 미연결이면 연결하고, 카운트 + 가중치 누적
    union(s, e)
    cnt += 1
    ans_weight += weight

print(ans_weight)