import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표 : 친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명 있는지 출력
# 알고리즘 : 유니온파인드!
# 집합에 몇 명 있는지 어떻게 체크? -> union by size 시스템 이용 

# 문자열로 주어짐 -> 딕셔너리로 구현 ?

import sys
input = sys.stdin.readline


def find_set(x):  # 대표 노드 찾아서 반환
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])  # 경로 압축
    return parents[x]

def union(x, y):  
    '''
    두 노드가 속한 집합 합치기
    합친 후의 네트워크 사이즈 반환!
    '''
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:  # 이미 같은 집합이면 패스
        return size[rep_x]
    
    if size[rep_x] > size[rep_y]:  # 사이즈가 더 큰 집합의 대표를 부모로 합치기
        size[rep_x] += size[rep_y]  # 사이즈 갱신
        parents[rep_y] = rep_x
        return size[rep_x]
    else:
        size[rep_y] += size[rep_x]
        parents[rep_x] = rep_y
        return size[rep_y]



T = int(input())
for tc in range(T):
    F = int(input())  # 친구 관계의 수

    # 유니온파인드 세팅
    parents = {}
    size = {}

    ans_list = []

    for _ in range(F):  # F줄의 친구 관계 : 두 사용자의 아이디 문자열
        a, b = input().split()
        for id in (a, b):
            if id not in parents:  # 처음 등장하는 이름인 경우 자기 자신을 부모로 새로 등록
                parents[id] = id
                size[id] = 1
        # 친구 집합 합치기
        network_size = union(a, b)
        # 친구 집합에 속한 사람 수 출력 -> ans_list에 모아서 한번에 출력! (매번 출력하는 것보다 효율적)
        ans_list.append(network_size)

    print('\n'.join(map(str, ans_list)))


