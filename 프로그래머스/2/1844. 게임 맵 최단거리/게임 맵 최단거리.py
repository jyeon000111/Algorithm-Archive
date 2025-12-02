# 목표: 
# - 맵에서 0은 벽, 1은 이동 가능.
# - 캐릭터는 처음에 좌상단 (0, 0)에 위치
# - 목적지는 우하단 (n-1, m-1)

# [ 아이디어 ] BFS
from collections import deque

def solution(maps):
    """
    maps: n * m 크기의 2차원 배열. 
    
    return: 캐릭터가 상대 팀 진영에 도착하기 위해 지나야 하는 최소 칸 수
    (도착 불가능하면 -1 리턴)
    """
    n = len(maps)  # 행 개수
    m = len(maps[0])  # 열 개수 
    
    # 상하좌우 이동
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    def bfs(starty, startx):
        visited = [[0] * m for _ in range(n)]  # 무한루프 방지 위해 방문 기록 (1이 방문)
        visited[starty][startx] = 1
        dq = deque([(starty, startx, 1)])  # (현재 좌표, 거쳐간 칸 수)
        
        while dq:
            nowy, nowx, move = dq.popleft()
            if (nowy, nowx) == (n - 1, m - 1):
                return move
            # 이동 가능한 칸 push
            for i in range(4):
                ny = nowy + dy[i]
                nx = nowx + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:  # 인덱스 범위 벗어나면 패스
                    continue
                if maps[ny][nx] == 0:  # 벽이면 패스
                    continue
                if visited[ny][nx] == 1:  # 방문했던 곳이면 패스
                    continue
                # 방문 표시 후 push
                visited[ny][nx] = 1
                dq.append((ny, nx, move + 1))
                
                
        return -1
    
    ans = bfs(0, 0)
    
    
    
    return ans