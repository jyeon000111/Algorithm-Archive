n, m = map(int, input().split())
# n행, m열 크기의 2차원 행렬 입력받기 (리스트 내부는 문자열 그대로 쓰기)
board = [] 
for row in range(n):
    board.append(input())

# 체스판의 가장 작은 구조 2가지
pattern1 = 'WBWBWBWB'
pattern2 = 'BWBWBWBW'

# 정상적인 체스판 패턴 2가지를 미리 만들어둔다.
chess_board_1 = []
for _ in range(4):
    chess_board_1.append(pattern1)
    chess_board_1.append(pattern2)
chess_board_2 = []
for _ in range(4):
    chess_board_2.append(pattern2)
    chess_board_2.append(pattern1)

# 목표: 8*8 크기로 잘라냈을 때, 다시 칠해야 하는 정사각형의 최소 개수
# 8*8의 왼쪽 모서리를 시작점으로 한다.
# 시작점이 될 수 있는 인덱스는 n-8, m-8이 최대!

# 시작점에서 8행, 8열에 대해서 2가지 패턴 각각에 대해서 다른 부분 발견하면 count한다.

for start_row in range(n - 7):
    for start_col in range(m - 7):
        current_difference_cnt = 0
        # 8행을 자른다.
        eight_lines = board[start_row:(start_row + 8)]
        # 각 줄에 대하여 start_col 기준으로 8글자를 자른다.
        for line in eight_lines:
            
            

