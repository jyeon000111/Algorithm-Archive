n, m = map(int, input().split())
# n행, m열 크기의 2차원 행렬 입력받기 (리스트 내부는 문자열 그대로 쓰기)
board = [] 
for row in range(n):
    board.append(input())


# 체스판 규칙에 따라 색칠되었는지, 어느 부분을 다시 칠해야 하는지 개수를 반환하는 함수를 만든다?? 
# (2가지 패턴을 모두 체크하고, 둘 중 작은 값을 반환)

def count_to_change_for_chess(square):
    '''8글자의 문자열 8개로 이루어진 리스트를 인자로 받아
    8행, 8열이 체스패턴에 맞게 칠해졌는지 확인하고,
    다시 칠해야 하는 개수를 반환하는 함수입니다.
    단, 체스패턴이 2가지가 가능하므로 
    각각 구해서 더 작은 값을 반환합니다.
    '''
    
    pattern1_count = 0  # W로 시작하는 패턴
    # (홀수, 홀수) = W, (짝수, 짝수) = W, (홀수, 짝수) = B, (짝수, 홀수) = B
    # 인덱스의 합이 짝수면, W, 홀수면 B여야 한다.
    # 규칙과 다르면 count +1 추가

    pattern2_count = 0  # B로 시작하는 패턴은 위와 반대의 경우에 카운트

    for row_idx, line in enumerate(square):
        for col_idx, char in enumerate(line):
            if (row_idx + col_idx) % 2 == 0:
                if char != 'W':
                    pattern1_count += 1
                else:
                    pattern2_count += 1
            else:
                if char != 'B':
                    pattern1_count += 1  
                else:
                    pattern2_count += 1

    return min(pattern1_count, pattern2_count)

# 가능한 8*8 행렬을 모두 탐색해서, 함수에 넣어보고, 작은 값을 재할당한다.
# 가능한 최댓값인 64로 초기화한다.
min_result = 64

# 8*8의 왼쪽 모서리를 시작점으로 한다.
# 시작점이 될 수 있는 인덱스는 n-8, m-8이 최대!

for start_row in range(n - 7):
    for start_col in range(m - 7):
        # 현재 8*8 정사각형 리스트를 만든다.
        current_square = []
        # 8행을 자른다.
        eight_lines = board[start_row:(start_row + 8)]
        # 각 줄에 대하여 start_col 기준으로 8글자를 자른다.
        for line in eight_lines:
            current_square.append(line[start_col:(start_col + 8)])
        # 현재 정사각형의 바꿔야할 최소 칸 수를 구한다.
        current_min = count_to_change_for_chess(current_square)
        if min_result > current_min:
            min_result = current_min

print(min_result)

