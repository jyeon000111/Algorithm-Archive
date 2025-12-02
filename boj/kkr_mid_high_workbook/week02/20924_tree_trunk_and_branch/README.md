## 1. 문제 정보 (Problem)

  - **문제 이름**: 트리의 기둥과 가지
  - **출처 및 번호**: [백준 20924번]('https://www.acmicpc.net/problem/20924')
  - **난이도**: 골드 4
  - **문제 요약**: 나무의 기둥의 길이와 가장 긴 가지의 길이 구하기

---
## 2. 핵심 아이디어 (Core Logic)


---
## 3. 어려웠던 점 (Difficulties)


---
## 4. 새롭게 배운 점 (What I Learned)


---
## 5. 코드 개선 (Refactoring)

- 첫번째 풀이 (런타임 에러)
```python
def dfs(now, len_from_root):
    '''
    파라미터: 현재 노드, 루트노드부터의 길이
    '''
    global max_length, giga_node, giga_length
    # 기가노드 찾기
    # 1. 루트노드이고, 인접노드 2개 이상
    # 2. 루트노드 아니고, 인접노드 3개 이상
    if giga_node == -1:  # 기가노드 아직 못 찾은 경우만 체크
        if (now == 'R' and len(tree[now]) >= 2) or (now != 'R' and len(tree[now]) >= 3):
            giga_node = now
            # 기둥 길이 구하기
            giga_length = len_from_root
    # print('현재노드:', now, '/ 루트부터 길이:', len_from_root, '/ 인접 노드 개수:', len(tree[now]), '/ 기가노드:', giga_node)
    for next, next_len in tree[now]:
        if visited[next]:
            continue
        visited[next] = 1
        dfs(next, len_from_root + next_len)
    else:  # 다음에 갈 노드가 없다 -> 리프노드
        # print('else 넘어온 now:', now)
        if giga_node == -1:  # 기가 노드 못 찾은 경우, 리프노드 = 기가노드
            giga_node = now
            giga_length = len_from_root
            # print('기둥길이', giga_length)

        branch_length = len_from_root - giga_length  # 가지의 길이 = 루트부터 리프까지 길이 - 루트부터 기가까지 길이
        if max_length < branch_length:  # 가지 길이의 최댓값 갱신
            max_length = branch_length
        return





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

dfs(R, 0)  # 루트노드부터 전위 순회

print(giga_length, max_length)
```

[ 문제점 + 개선할 점 ] 
1. for - else 문에서 else문 이후의 리프노드 확인 코드가 매번 실행되고 있음
  - break 가 없으면 항상 else문이 돌아감
  => 자식 노드의 수(미방문 인접 노드)가 0인 경우를 체크하는 코드로 변경
2. 재귀 깊이 제한 문제 (노드 개수 N이 20만까지 주어짐)
  => BFS 또는 스택으로 구현

- 두번째 풀이 (시간 초과)
```python
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
```

[ 문제점 + 개선할 점 ]
1. 기가노드까지 한개씩 계속 큐에 넣었다 뺐다 하면서 비효율 발생
   => 자식노드 수 2개 이상되거나 리프노드 도달할 때까지 while문으로 쭉 내려가기 
2. len으로 매번 자식노드 수 계산 하지말고, 미리 구해두기 
   (루트노드는 인접 노드 수, 루트노드 아니면 인접 노드 수 - 1)
3. 기가노드부터 리프노드까지 BFS 돌리면서 최대 길이 갱신
4. input() 함수는 10만 개 이상 입력 받을 경우 시간 초과 발생!!!
    => sys.stdin.readline() 사용! 
    ```python
    import sys
    input = sys.stdin.readline
    ```

### 최종 코드
```python
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
```