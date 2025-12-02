N = int(input())

# 목표: 크기 N*N 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 방법의 수 출력
# 퀸은 상하좌우, 대각선 8방향으로 원하는 만큼 이동 가능
# 1. 일단 좌우 방향에 걸리는 경우 제외 -> 행마다 하나씩 놓기
# 2. 상하 걸리는 경우 제외 -> visited_col 배열으로 방문 표시
# 3. 대각선 걸리는 경우 제외 -> visited_diag1(행-열), visited_diag2(행+열) 배열로 방문 표시
#   - 좌상향 대각선은 행-열 이 일정하고, 우상향 대각선은 행+열 이 일정함
result_cnt = 0  # 경우의 수 카운트 변수 초기화
visited_col = [False] * (N+1)
visited_left_diag = set()  # 행 인덱스 - 열 인덱스 의 값 저장
visited_right_diag = set()  # 행 인덱스 + 열 인덱스 의 값 저장

def place_queens(row):
    '''퀸을 놓을 행을 인자로 받아
    N-1 행까지 놓는 경우의 수를 카운트하는 함수입니다.
    '''
    global result_cnt

    if row == N:  # N-1행까지 다 놓으면
        result_cnt += 1
        return

    # 퀸은 무조건 행마다 하나씩 놓는다. 
    i = row

    # 열 인덱스를 모두 탐색한다.
    for j in range(N):
        # 1. 열 인덱스가 겹치지 않고,
        # 2. visited_left_diag, visited_right_diag 리스트에 i-j, i+j 값이 없으면,
        if not visited_col[j]:  
            if (i-j) not in visited_left_diag and (i+j) not in visited_right_diag:
                
                # 놓은 후, 해당 열, 두 가지 대각선 방문 표시
                visited_col[j] = True
                visited_left_diag.add(i-j)
                visited_right_diag.add(i+j)
                
                # 다음 행으로 재귀호출
                place_queens(row + 1)

                # 돌아와서 놓은 퀸 회수 후, 해당 열 방문 흔적 삭제
                visited_col[j] = False
                visited_left_diag.remove(i-j)
                visited_right_diag.remove(i+j)


place_queens(0)
print(result_cnt)