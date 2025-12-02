## 1. 문제 정보 (Problem)

  - **문제 이름**: 타임머신
  - **출처 및 번호**: [백준 11657]('https://www.acmicpc.net/problem/11657')
  - **난이도**: 골드 4
  - **문제 요약**: 

---
## 2. 핵심 아이디어 (Core Logic)
음수 가중치 존재할 때의 최단 거리
- 하나의 출발점(1)에서 다른 모든 정점까지의 최단 거리 + 음수 사이클 감지(무한히 음수로 작아지면 -1 출력) => 벨만포드 알고리즘


---
## 3. 어려웠던 점 (Difficulties)


---
## 4. 새롭게 배운 점 (What I Learned)
### 음수 가중치 존재할 때, 최단경로 찾기
- 다익스트라는 음수 가중치가 있을 땐 사용 불가능 
- 음수 간선이 포함되면, 벨만-포드 또는 플로이드-워셜 

### Bellman-Ford 알고리즘
- 목적: 하나의 시작 정점에서 다른 모든 정점까지의 최단 거리 (Single Source Shortest Path, SSSP)
  - 1:N (하나의 출발점)
- 음수 사이클(Negative Cycle) 감지
  - 음수 사이클: 돌수록 비용이 계속 줄어드는 무한 루프 -> 최단 거리 정의 불가능! 
- 동작 방식: 모든 간선(E개)를 V-1(V는 정점 수)번 확인하면서 최단 거리를 계속 갱신. V번째에도 갱신 일어나면 음수 사이클 존재함을 의미
- 시간 복잡도: O(V*E)
```python
def bellman_ford(start, v_cnt, edges):
    '''
    start: 시작 노드 번호
    v_cnt: 총 노드 개수
    edges: (출발, 도착, 비용) 튜플의 리스트

    return: 음수사이클 존재 여부(T/F), 최종 거리 리스트
    '''

    # 1. 거리 배열 초기화
    dist = [float('inf')] * (v_cnt + 1)  # 노드 번호 1부터 사용한다고 가정
    dist[start] = 0 

    # 2. (V-1)번 만큼 모든 간선 확인 + V번째 음수 사이클 확인 => 총 V번 반복
    for i in range(v_cnt):
        # 매 반복마다 모든 간선 순회
        for u, v, cost in edges:
            # u가 도달 가능한 노드(무한대가 아님)여야 함
            # v로 가는 기존 경로(dist[v])보다 u를 거쳐 가는 경로(dist[u] + cost)가 더 짧다면 갱신
            if dist[u] != float('inf') and dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost

                # 3. V번째 반복에도 갱신이 일어난다면?
                # => 음수 사이클이 존재한다는 뜻!
                if i == v_cnt - 1:
                    return True, None  # (음수 사이클 있음, 거리 리스트 없음)
    
    # 4. V번 반복 후에도 갱신이 없었다면 (음수 사이클 X)
    return False, dist  # (음수 사이클 없음, 최종 거리 리스트)


# V는 노드 수, E는 정점 수
# edges는 간선 리스트 (출발, 도착, 비용)

has_negative_cycle, distances = bellman_ford(start_node, V, edges)


if has_negative_cycle:
    print("음수 사이클이 존재한다.")
else:
    print(f"시작 노드 {start_node}로부터의 최단 거리:")
    for i in range(1, V+1):


```



### Floyd-Warshall 알고리즘
- 목적: 모든 정점 쌍 간의 최단 거리 (All Pairs Shortest Path, APSP)
  - N:N (모든 쌍)
- DP 기법 사용
- 동작 방식: 3중 반복문 사용. k라는 중간 경유지 설정하고, 'i에서 j로 바로 가는 거리'와 'i에서 k를 거쳐 j로 가는 거리'를 비교해서 더 짧은 값으로 갱신
- 시간 복잡도: O(V^3)

```python
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```





---
## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
def bellman_ford(start):
    '''
    출발노드 번호를 인자로 받아,
    나머지 도시로 가는 최단 시간을 구한다.
    (음수사이클 발견여부(T/F), 최단거리 리스트) 를 반환한다.
    '''

    dists = [INF] * (N+1)
    dists[start] = 0

    for i in range(1, (N+1)):  # N번 반복(N번부터의 갱신은 음수 사이클 신호!) 
        for s_node, e_node, cost in edges:  # 모든 간선 확인
            if dists[s_node] == INF:  # 출발노드가 아직 도달하지 못한 노드면 패스
                continue
            if dists[e_node] > dists[s_node] + cost:  # 도착노드까지 기록된 최단거리보다 현재 간선 거쳐 가는게 짧으면 갱신
                dists[e_node] = dists[s_node] + cost
                if i == N:  # N번째 갱신 발생한 경우
                    return True, None
    
    return False, dists
```

- 개선할 점: 한 바퀴 완화(Relaxation)에서 갱신이 한 번도 없으면 반복 즉시 종료 -> 성능 개선

- 최종 코드
```python
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
```

- 리팩토링 결과
![boj_11657_result](boj_11657_result.png)
