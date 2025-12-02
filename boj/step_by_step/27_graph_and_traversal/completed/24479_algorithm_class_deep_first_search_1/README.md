## 1. 문제 정보 (Problem)

  - **문제 이름**: 알고리즘 수업 - 깊이 우선 탐색 1
  - **출처 및 번호**: [백준 24479번]('https://www.acmicpc.net/problem/24479')
  - **난이도**: 실버 2
  - **문제 요약**:  정점 R에서 시작하여 깊이 우선 탐색할 경우, 1~N번 정점의 방문 순서 출력 (방문할 수 없는 경우 0 출력)

---
## 2. 핵심 아이디어 (Core Logic)
- DFS를 재귀 함수로 구현
- 인접 리스트 방식으로 그래프 저장
- visit_order 리스트에 정점의 방문 순서 기록. visited 배열을 대체.
- 전역 카운터: 방문 순서를 체크하기 위해 전역 변수 cnt 사용 
- 오름차순 방문 이라는 조건을 만족시키기 위해, 각 정점의 인접 리스트를 오름차순으로 정렬.
  - map(), sorted() 함수 함께 사용.


---
## 3. 어려웠던 점 (Difficulties)
- 백준 채점 결과 RecursionError 발생 
  - 파이썬은 재귀 호출 깊이를 최대 1,000회 정도로 제한
  - 이 문제에선 정점의 개수가 최대 100,000개

- 시간 초과 발생 
  - 방문한 정점을 순서대로 리스트에 저장하고, 다시 index 메서드로 방문 순서를 계산함.
  - index 메서드가 리스트 전체를 탐색해 한 번 실행에 O(N) 시간복잡도를 가짐.

---
## 4. 새롭게 배운 점 (What I Learned)
- 재귀 호출 제한 늘리는 방법
```python
import sys
sys.setrecursionlimit(10**6) # 재귀 깊이를 1,000,000으로 설정
```

- index 메서드가 시간복잡도 면에서 비효율적이라는 걸 새로 배웠다.

---
## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
def dfs(now):
    '''
    현재 정점을 인자로 받아,
    깊이 우선탐색을 하면서,
    각 정점에 방문 순서를 기록하는
    재귀 함수입니다.
    '''
    node_visit_list.append(now)

    for next in graph[now]:
        # 미방문인 인접 정점에 대해 방문 표시하고, 재귀호출
        if not visited[next]:
            visited[next] = True
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

node_visit_list = []
visited = [False] * (N+1)  # 인덱스가 정점 번호. 방문 여부 저장
visited[R] = True # 시작 정점 방문 표시
dfs(R)

# 정점 a의 방문 순서는 node_visit_list의 인덱스 위치 + 1 과 같다.
for i in range(1, N+1):
    try:
        print(node_visit_list.index(i) + 1)
    except:  # 존재하지 않는 경우, 0 출력
        print(0)
```
- 문제점: 
  - node_visit_list에 방문한 노드를 순서대로 추가하고, index()로 몇 번째 방문인지 찾고 있음
  - `.index()` 메서드는 리스트 전체를 탐색해야 해서 시간이 오래 걸림(O(N)). 이 작업을 N번 반복해서 출력 부분에서만  O(N^2) 시간이 걸림.

- 개선한 코드
  - 정점별 방문 순서를 리스트에 바로 저장. (인덱스를 정점 번호로 값을 방문 순서로 저장)
  - visited 배열을 없애고, visit_order 배열에 방문 순서를 기록.
    - 값이 0이면 미방문, 0이 아니면 방문을 의미
  - 방문 순서를 카운트 하기 위해 전역 변수 관리
```python
import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기
input = sys.stdin.readline  # 시간 초과 방지

def dfs(now):
    global cnt
    '''
    현재 정점을 인자로 받아,
    깊이 우선탐색을 하면서,
    방문한 정점을 리스트에 순서대로 저장하는
    함수입니다.
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
```