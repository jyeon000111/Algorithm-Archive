import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기
input = sys.stdin.readline  # 시간 초과 방지

def dfs(now):
    global cnt
    '''
    현재 정점을 인자로 받아,
    깊이 우선탐색을 하면서,
    각 정점에 방문 순서를 기록하는
    재귀 함수입니다.
    '''
    for next in graph[now]:
        # 미방문인 인접 정점에 대해 방문 표시하고, 재귀호출
        if not visit_order[next]:
            cnt += 1
            visit_order[next] = cnt
            dfs(next)


N, M, R = map(int, input().split())
# 정점의 수 N, 간선의 수 M, 시작 정점 R

# 목표: 정점 R에서 시작하여 깊이 우선 탐색할 경우, 1~N번 정점의 방문 순서 출력 (방문할 수 없는 경우 0 출력)
# - 인접 정점은 오름차순 방문

# 정점 집합: 1번~N번
nodes = list(range(1, N+1))

graph = [[] for _ in range(N+1)]  # 무방향 그래프 인접 리스트로 저장 (인덱스가 정점 번호, 인접 정점을 리스트로 저장)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 양방향 간선

# 오름차순 방문을 위해, graph의 모든 리스트를 오름차순 정렬한다.
graph = list(map(sorted, graph))

visit_order = [0] * (N+1)  # 인덱스가 정점 번호. 방문 순서 저장. 0이면 방문하지 않은 것
visit_order[R] = 1 # 시작 정점 방문 표시 (순서 1)
cnt = 1  # 방문한 정점 개수

dfs(R)

for order in visit_order[1:]:
    print(order)
