import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: 1 a b => a와 b가 같은 집합에 포함되어 있으면 'YES' / 그렇지 않으면 'NO' 출력
# - n+1 개의 집합 : {0}, {1}, {2}, ..., {n}
# 0 a b  => a가 포함된 집합, b가 포함된 집합을 합친다.

# 유니온 파인드 -> 트리 자료구조로 구현
def make_set(x):
    '''
    x를 원소로 가진 집합 생성
    '''
    parent[x] = x
    rank[x] = 0

def find_set(x):
    '''
    x가 속한 집합의 대표 원소 반환
    '''
    # To-do: 각 원소의 대표원소를 최종 대표 원소로 변경 (경로 압축)
    if x != parent[x]:
        parent[x] = find_set(parent[x])

    return parent[x]



def union(x, y):
    '''
    y가 속한 집합과 x가 속한 집합의 합집합을 만든다.
    '''
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:  # 이미 같은 집합에 속해 있는 경우
        return

    if rank[root_x] > rank[root_y]:  # x 트리의 높이가 더 높으면, x를 y의 부모로 저장
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1




n, m = map(int, input().split())
parent = [-1] * (n+1)  # 노드 x의 부모 저장
rank = [-1] * (n+1)  # 루트 노드가 x인 트리의 랭크 값 저장

for i in range(n+1):  # 0 ~ n+1 까지 원소 1개인 집합 생성
    make_set(i)

for _ in range(m):  # m 개의 연산
    tokens = list(map(int, input().split()))
    if tokens[0] == 0:  # 집합 합치기
        union(tokens[1], tokens[2])
    else:  # 같은 집합 포함 여부 출력
        if find_set(tokens[1]) == find_set(tokens[2]):
            print('YES')
        else:
            print('NO')
