import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: 1번 도시에서 출발해서 나머지 도시로 가는 최단 시간 구하기
# [출력] 
# - 1, 2, 3, .., N번 도시로 가는 최단 시간 출력 (단, 해당 도시로 가는 경로 없다면 -1 출력)
# - 1번에서 어떤 도시로 가는 과정에서 시간을 무한히 음수로 감소시킬 수 있다면(음수 사이클 존재) -1 출력

# [아이디어]
# - 이동 시간은 양수가 아닌 경우도 있다. 0 또는 음수일 수 있다!
#   - 가중치가 음수 -> 다익스트라 불가능! 
# => 벨만포드 알고리즘 (음수 가중치 + 음수 사이클 탐지 + 하나의 출발점 1:N의 최단거리)

import sys
input = sys.stdin.readline

INF = float('inf')  # 무한대 상수

def bellman_ford(start):
    '''
    출발노드 번호를 인자로 받아,
    나머지 도시로 가는 최단 시간을 구한다.
    (음수사이클 발견여부(T/F), 최단거리 리스트) 를 반환한다.
    '''

    dists = [INF] * (N+1)
    dists[start] = 0

    for i in range(1, (N+1)):  # N번 반복(N번부터의 갱신은 음수 사이클 신호!) 
        updated = False  # 이번 라운드의 갱신 발생 여부 (조기 종료 조건)
        for s_node, e_node, cost in edges:  # 모든 간선 확인
            if dists[s_node] == INF:  # 출발노드가 아직 도달하지 못한 노드면 패스
                continue
            if dists[e_node] > dists[s_node] + cost:  # 도착노드까지 기록된 최단거리보다 현재 간선 거쳐 가는게 짧으면 갱신
                dists[e_node] = dists[s_node] + cost
                updated = True
                if i == N:  # N번째 갱신 발생한 경우
                    return True, None
        if not updated:  # 한 바퀴 돌아도 갱신 없음 => 조기 종료
            break  # for i

    
    return False, dists


N, M = map(int, input().split())  # N은 도시(노드) 수, M은 버스 노선(간선) 수
edges = []  # (출발노드, 도착노드, 가중치)
for _ in range(M):
    # a는 출발도시, b는 도착도시, c는 이동시간
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

has_negative_cycle, dist_list = bellman_ford(1)

if has_negative_cycle:
    print(-1)
else:
    for node in range(2, N+1):
        if dist_list[node] == INF:
            print(-1)
        else:
            print(dist_list[node])