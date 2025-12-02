import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------



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
