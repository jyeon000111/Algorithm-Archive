## 1. 문제 정보 (Problem)

  - **문제 이름**: 상근이의 여행
  - **출처 및 번호**: [백준 9372번]('https://www.acmicpc.net/problem/9372')
  - **난이도**: 실버 4
  - **문제 요약**: 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수

---
## 2. 핵심 아이디어 (Core Logic)
"주어지는 비행 스케줄은 항상 연결 그래프를 이룬다."
-> 정점 간에 무조건 이동 가능한 간선 존재

N개의 정점을 연결하기 위한 최소 간선 수: N - 1 개

---
## 3. 어려웠던 점 (Difficulties)
- 연결 그래프라는 조건을 제대로 이해하지 못해서, 어려운 방법으로 풀었다.
    - 처음 아이디어
      - 최소 신장 트리: 최소 간선으로 모든 국가 연결
      - 유니온파인드로 연결 여부 확인
      - 인접 정점 수가 적은 곳부터 연결 (1개짜리는 무조건 연결해야 함)

---
## 4. 새롭게 배운 점 (What I Learned)


---
## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
# 최소 신장 트리: 최소 간선으로 모든 국가 연결
# 유니온파인드로 연결 여부 확인
# 인접 정점 수가 적은 곳부터 연결 (1개짜리는 무조건 연결해야 함)


def find_set(x):
    if x == p[x]:
        return x
    p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry:
        return

    p[ry] = rx


T = int(input())  # 테스트케이스 수
for _ in range(T):
    N, M = map(int, input().split())  # N은 국가 수(1~N번), M은 비행기 수
    graph = [[] for _ in range(N + 1)]  # 인접리스트: 정점 번호를 인덱스로 인접한 정점 저장
    for _ in range(M):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)  # 양방향

    # 유니온파인드 자료구조
    p = [num for num in range(N+1)]

    min_cnt = 0  # 간선의 최소 개수

    for s in range(N+1):
        if not graph[s]:  # 빈리스트 건너뛰기
            continue
        for e in graph[s]:  # 인접 정점 (연결 안 돼있으면 연결)
            if find_set(s) != find_set(e):
                union(s, e)
                min_cnt += 1

    print(min_cnt)
```

- 문제점: 연결그래프에서 모든 정점을 연결하기 위한 최소 간선 수는 N-1개로 고정되어 있음.
    - 유니온파인드 kruskal 같은 복잡한 연산이 불필요함.
    
```python
T = int(input())  # 테스트케이스 수
for _ in range(T):
    N, M = map(int, input().split())  # N은 국가 수(1~N번), M은 비행기 수
    for _ in range(M):
        input()
    
    # 모든 정점을 연결하는 최소 간선 수는 N-1 개
    print(N-1)
```