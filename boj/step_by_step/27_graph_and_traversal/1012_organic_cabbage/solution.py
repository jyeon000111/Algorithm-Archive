from collections import deque

def bfs_cabbage(i, j):
    global cnt
    '''
    배추가 있는 행, 열 인덱스를 인자로 받아,
    이동 가능한 인접 배추를 카운트하고,
    카운트한 인접 배추를 0으로 변경하는
    함수입니다. 
    '''
    dq = deque([(i, j)])  # 탐색할 배추 목록
    while dq:
        nowi, nowj = dq.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = nowi+di, nowj+dj
            if 0<=ni<N and 0<=nj<M and farm_arr[ni][nj] == 1:
                dq.append((ni, nj))
                farm_arr[ni][nj] = 0  # 탐색 처리
                cnt += 1  # 인접 배추 추가하면서 카운트


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # 배추밭 N*M 사이즈, 배추 개수 K개
    farm_arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        farm_arr[i][j] = 1  # 배추 위치 1로 표시

    # 목표: 배추흰지렁이가 상하좌우 인접한 배추로 이동 가능할 때, 모든 배추를 관리하기 위해 필요한 최소 지렁이 수 출력
    # 좌상단 기준으로 이동 가능한 인접 배추 모두 덱에 담아둔 후, 0으로 변경하고, 카운트. => visited 배열 불필요
    # K - 카운트한 수 = 답

    cnt = 0

    for i in range(N):
        for j in range(M):
            if farm_arr[i][j] == 1:
                farm_arr[i][j] = 0  # 탐색 시작 배추 다시 탐색하지 않도록 처리
                bfs_cabbage(i, j)

    print(K - cnt)

