import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------
# 목표: Q개의 커맨드 하나마다 목적지에 도달할 수 있다면 1, 아니면 0을 공백으로 구분해 출력
# - 커맨드 전부 실행 후, 목적지에 위치해 있는지 (목적지 이동 가능 여부 X)
# [필드 정보] G는 이동 가능 / T는 이동 불가 / X는 출발지 / Y는 목적지
# [조종 동작] A는 앞으로 이동(나무 있거나 필드 벗어나면 아무 일 X) / L 왼쪽으로 90도 회전 / R 오른쪽으로 90도 회전

# - 항상 위를 바라보는 방향으로 조종 시작

dy = [-1, 0, 1, 0]  # 상 우 하 좌 (오른쪽으로 회전하는 순서)
dx = [0, 1, 0, -1]

def find_start():
    '''출발지의 좌표를 반환하는 함수'''
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                return i, j

def move(C, command):

    dir = 0  # 0: 상 / 1: 우 / 2: 하 / 3: 좌
    now_y = start_i
    now_x = start_j

    for i in range(C):
        if command[i] == 'A':  # 앞으로 이동
            next_y = now_y + dy[dir]
            next_x = now_x + dx[dir]
            # 맵 벗어나는 경우 다음 조종으로
            if next_y < 0 or next_y >= N or next_x < 0 or next_x >= N:
                continue
            # 나무 T인 경우 다음 조종으로
            if field[next_y][next_x] == 'T':
                continue
            now_y = next_y  # 이동
            now_x = next_x

        elif command[i] == 'L':
            dir = (dir + 3) % 4

        else:  # R 일 때
            dir = (dir + 1) % 4

    if field[now_y][now_x] == 'Y':  # 목적지 도착하는 경우
        return 1
    else:
       return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 필드의 크기
    field = [list(input()) for _ in range(N)]

    Q = int(input())  # 조종한 횟수

    start_i, start_j = find_start()  # 출발지 찾기


    ans = []

    for _ in range(Q):  # Q개의 줄에 걸쳐 커맨드 길이, 커맨드가 주어짐
        C, command = input().split()
        C = int(C)
        ans.append(move(C, command))

    print(f'#{tc}', *ans)
