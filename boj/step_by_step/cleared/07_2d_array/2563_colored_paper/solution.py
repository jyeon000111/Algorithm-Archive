num_paper = int(input())
# 100*100 2차원 배열을 0으로 초기화해서 흰 도화지를 표현한다.
white_paper = [[0]*100 for _ in range(100)]

for paper in range(num_paper):
    distance_left_side, distance_bottom_side = map(int, input().split())
    # 색종이가 붙은 영역을 1로 바꾼다.
    # 헷갈리니까, 도화지를 아래 위로 뒤집었다 치고, 
    # 아래쪽 변과의 거리가 0인 걸 0행부터 시작하는 걸로 가정한다.
    # 예) 왼쪽 변, 아래쪽 변과의 거리가 모두 0이면,
    #   - 0행 0열부터 9행 9열까지 1로 바꾼다.
    # 예2) 왼쪽 변과의 거리 l, 아래쪽 변과의 거리 b면,
    #   - b행 l열부터 (b+9)행 (l+9)열까지 1로 바꾼다.
    for row_idx in range(distance_bottom_side, distance_bottom_side + 10):
        for col_idx in range(distance_left_side, distance_left_side + 10):
            white_paper[row_idx][col_idx] = 1

# 이중 리스트의 모든 요소의 합을 구한다.
total_area = 0
for row in white_paper:
    total_area += sum(row)

print(total_area)