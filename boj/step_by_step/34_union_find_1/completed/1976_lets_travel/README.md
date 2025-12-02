## 1. 문제 정보 (Problem)

  - **문제 이름**: 여행 가자
  - **출처 및 번호**: [백준 1976번]('https://www.acmicpc.net/problem/1976')
  - **난이도**: 골드 4
  - **문제 요약**: 도시들간의 인접 행렬이 주어졌을 때, 여행 경로가 가능하면 YES, 불가능하면 NO 출력

---
## 2. 핵심 아이디어 (Core Logic)
- 유니온 파인드 자료구조 활용
- 여행 경로가 모두 같은 집합에 속하면 여행 가능!
- 그래프 연결성 판별 문제!


---
## 3. 어려웠던 점 (Difficulties)


---
## 4. 새롭게 배운 점 (What I Learned)
- 그래프 연결성 판별 문제 -> BFS, DFS로도 풀 수 있음. / 유니온파인드가 자연스럽고 효율적인 풀이.

### 유니온파인드 문제 구별
=> 여러 개의 원소를 몇 개의 그룹으로 묶고, 두 원소가 같은 그룹에 속하는지 아주 빠르게 확인
1. '같은 집합', '같은 그룹', '연결 요소'
2. 실시간으로 연결하고 합치는 연산(Union)이 필요할 때
3. 크루스칼 알고리즘 사용해 최소 신장 트리 (MST) 구하는 문제
4. 그래프에서 '사이클'이 생기는지 판별할 때
  - 간선을 하나씩 추가하면서 사이클 발생 여부 확인
  - 두 노드의 대표 노드가 이미 같다면, 연결된 노드므로 간선 추가하면 사이클 발생!



---
## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
N = int(input())  # 도시의 수  (1~N번)
M = int(input())  # 여행 계획에 속한 도시들의 수

parents = [num for num in range(N+1)]
ranks = [0] * (N+1)

graph = [list(map(int, input().split())) for _ in range(N)]  # 인접행렬 (1이면 연결, 0이면 연결X)

for i in range(1, N+1):  # i번 도시와 j번 도시의 연결 정보 -> i와 j 집합 합치기
    for j in range(1, N+1):
        if graph[i-1][j-1]:
            union(i, j)


travel_path = list(map(int, input().split()))  # 여행 경로

ans = True  # 여행 가능하다고 가정

for idx in range(M-1):
    if find_set(travel_path[idx]) != find_set(travel_path[idx + 1]):  # 같은 집합이 아니면 여행 불가
        ans = False
        break  # for idx

if ans:
    print('YES')
else:
    print('NO')
```

문제점
- 여행 가능 여부 판단할 때, 인접 경로를 하나씩 확인할 필요 없음
    - 어차피 모두 같은 집합에 속해야 하므로, 첫번째 도시의 루트 노드를 구하고, 이후의 도시들의 루트 노드가 동일한지 체크하면 됨.
- 인접행렬 그래프를 순회할 때, graph[i][j] == graph[j][i] 동일함.
    - 같은 정보를 중복으로 탐색하고 있음.
    - j 의 범위를 range(i+1, N+1)로 변경하면 중복 탐색이 사라짐.
    

- 최종 코드
```python
# 목표: 여행 경로가 가능하면 YES, 불가능하면 NO 출력
# - 중간에 다른 도시를 경유해도 됨. 같은 도시 여러 번 방문 가능.

# 유니온 파인드: 같은 집합에 속해 있으면 여행 가능.

def find_set(x):
    '''
    x의 루트 노드 반환
    '''
    if x == parents[x]: # 본인이 루트 노드면 바로 반환
        return x

    parents[x] = find_set(parents[x])  # 경로 압축
    return parents[x]

def union(x, y):
    '''
    x, y 가 속한 집합 합치기
    '''
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:  # 같은 집합이면 패스
        return

    if ranks[rep_x] > ranks[rep_y]:  # x 대표자의 랭크가 더 높으면 rep_x를 대표자로 합치기
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y
        if ranks[rep_x] == ranks[rep_y]:  # x, y 대표자 랭크가 같으면 대표자로 설정한 루트의 랭크 1 증가
            ranks[rep_y] += 1


N = int(input())  # 도시의 수  (1~N번)
M = int(input())  # 여행 계획에 속한 도시들의 수

parents = [num for num in range(N+1)]
ranks = [0] * (N+1)

graph = [list(map(int, input().split())) for _ in range(N)]  # 인접행렬 (1이면 연결, 0이면 연결X)

for i in range(1, N+1):  # i번 도시와 j번 도시의 연결 정보 -> i와 j 집합 합치기
    for j in range(i+1, N+1):  # 중복 탐색 줄이기
        if graph[i-1][j-1]:
            union(i, j)


travel_path = list(map(int, input().split()))  # 여행 경로

ans = True  # 여행 가능하다고 가정

rep_first = find_set(travel_path[0])  # 첫번째 도시의 대표자
for idx in range(1, M):
    if find_set(travel_path[idx]) != rep_first:  # 같은 집합이 아니면 여행 불가
        ans = False
        break  # for idx

if ans:
    print('YES')
else:
    print('NO')
```