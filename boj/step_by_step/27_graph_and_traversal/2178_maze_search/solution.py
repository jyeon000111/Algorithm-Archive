from collections import deque

def bfs(starti, startj):
    '''
    시작점 행, 열 인덱스를 인자로 받아
    (N,M) 위치에 도달할 때까지
    너비 우선 탐색을 진행하고,
    이 때의 최소 이동 칸 수를 반환하는 함수입니다.
    '''
    dq = deque([(starti, startj)])

    while dq:
        nowi, nowj = dq.popleft()
        if (nowi, nowj) == ((N-1), (M-1)):  # 도착점에 도달하면, 이동 칸수 반환하고 종료
            return visited[nowi][nowj]

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = nowi+di, nowj+dj
            if 0<=ni<N and 0<=nj<M and maze[ni][nj] == 1 and visited[ni][nj] == 0:  # 방문하지 않은 인접정점
                visited[ni][nj] = visited[nowi][nowj]+1  # 방문 처리+ 거리 정보 함께 저장
                dq.append((ni, nj))


N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]  # N*M 배열 미로

# 목표: (1,1)에서 (N,M) 위치로 이동할 때 지나야 하는 최소 칸 수 출력 (항상 도달 가능)
# - 1은 이동 가능, 0은 이동 불가
# => 최소 이동거리를 구해야 하므로, BFS 활용

visited = [[0]*M for _ in range(N)]
visited[0][0] = 1  # 시작점 좌표 방문 처리

ans = bfs(0, 0)
print(ans)