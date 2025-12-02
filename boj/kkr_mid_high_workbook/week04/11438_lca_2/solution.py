import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: M개의 줄에 차례대로 입력받은 두 노드의 가장 가까운 공통 조상 구하기
# N개의 정점(1~N번)으로 이루어진 트리 (루트는 1번)

# 트리를 어떻게 저장할 것인가.. -> 인접리스트?
# 공통 조상 구하려면? 매번 거슬러올라가야 하나? -> 최악의 경우 N*M = (10^5)^2 = 10^10
# - 파이썬은 1초에 3천만(3*10^7)번 연산 가능하다고 가정 => 무조건 시간초과

# [알고리즘] Binary Lifting 기반 LCA
# - 2^k칸씩 점프 (미리 2^k번째 조상 테이블 DP로 만들어두기)
# - 같아지기 직전까지 점프 -> 바로 위 부모가 LCA
# 시간복잡도 : O((N+M)logN), 최악의 경우 20만 * 17 = 약 340만 (1초도 안 걸림!)


import math
import sys 
input = sys.stdin.readline


def dfs(start):
    '''
    시작 노드를 인자로 받아,
    스택 기반의 DFS 탐색을 통해, 
    i의 부모 노드를 찾아 parent[0][i]에 기록한다.
    깊이도 depth 배열에 기록한다.
    '''
    stack = [start]
    depth[start] = 0

    while stack:
        now = stack.pop()
        for next in graph[now]:
            if depth[next] != -1:  # 이미 부모 노드 찾은 경우(=방문함), 패스
                continue
            parent[0][next] = now
            depth[next] = depth[now] + 1
            stack.append(next)



N = int(input())  # N은 노드의 수

LOG = math.ceil(math.log2(N))

graph = [[] for _ in range(N+1)]  # 인접리스트
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)  # 무방향


# DP 
parent = [[-1] * (N+1) for _ in range(LOG+1)]  # k는 log10^5(대략 16)까지 가능. 
depth = [-1] * (N+1)  # 깊이(레벨) 배열
# 1. parent[0][i] = i의 부모노드
# 부모 찾기 DFS
dfs(1)  # 루트노드에서 출발


# 2. parent[k][i] = i의 2^k번째 조상노드 
# = i의 2^(k-1)번째 조상노드의 2^(k-1)번째 조상노드 = parent[k-1][ parent[k-1][i] ]
# 2^k = 2^(k-1) + 2^(k-1)

for k in range(1, LOG+1):
    for i in range(2, (N+1)):
        if parent[k-1][i] == -1:  # 부모가 없으면 패스
            continue
        parent[k][i] = parent[k-1][ parent[k-1][i] ]


# LCA 찾기 쿼리
ans_list = []
M = int(input())  # M은 쿼리의 수
for _ in range(M):
    v1, v2 = map(int, input().split())
    # 1. 깊은 레벨의 노드 점프시켜서 같은 레벨에 위치시키기
    # v1이 더 깊다고 가정
    if depth[v1] < depth[v2]:
        v1, v2 = v2, v1
        
    diff = depth[v1] - depth[v2]
    
    for j in range(LOG, -1, -1):
        if diff & (1 << j):
            diff -= 1 << j
            v1 = parent[j][v1]
    if v1 == v2:  # 깊이 맞춘 후, 같은 노드일 때 => LCA 는 v2
        ans_list.append(v1)
    else:
        # 2. 두 노드 같아지기 직전까지 함께 점프시키기 (점프 폭 줄여가기)
        for i in range(LOG, -1, -1):
            if parent[i][v1] != parent[i][v2]:
                v1 = parent[i][v1]
                v2 = parent[i][v2]
        
        ans_list.append(parent[0][v1])

print('\n'.join(map(str, ans_list)))
        
            
            