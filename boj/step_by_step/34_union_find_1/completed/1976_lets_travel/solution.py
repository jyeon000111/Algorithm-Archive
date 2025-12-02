import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

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







