import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------
# 목표: 잘라진 하얀색 색종이의 개수 / 파란색 색종이의 개수 출력

# - 모두 같은 색이 아니면 4등분 -> 잘린 조각들에 대해서도 반복 -> 모두 같은 색이 되거나, 하나의 칸이 될 때까지 반복
#
def recur(cur_r, cur_c, cur_size):
    '''
    종이 배열의 좌상단 꼭짓점 좌표와 한 변의 길이를 인자로 받는다.
    종이가 모두 같은 색인지 확인하고, 같은 색이면 색깔별로 카운트한다.
    다른 색이 섞여 있으면 4등분해서 재귀호출한다.
    '''
    global white_cnt, blue_cnt

    # 좌상단 꼭짓점의 색을 기준으로 모두 동일한지 비교
    cur_color = paper_arr[cur_r][cur_c]

    is_equal = True
    if cur_size > 1:
        for di in range(cur_size):
            for dj in range(cur_size):
                if paper_arr[cur_r + di][cur_c + dj] != cur_color:
                    is_equal = False
                    break   # for dj
            if not is_equal:
                break   # for di

    # 모두 같은 색인 경우
    if is_equal:
        if cur_color == 0:
            white_cnt += 1
        else:
            blue_cnt += 1
        return

    # 색깔이 섞여 있는 경우
    else:
        next_size = cur_size // 2
        for dr, dc in [(0, 0), (0, next_size), (next_size, 0), (next_size, next_size)]:
            next_r = cur_r + dr
            next_c = cur_c + dc
            recur(next_r, next_c, next_size)




N = int(input())  # 종이의 한 변의 길이 N (2, 4, 8, 16, 32, 64, 128)
paper_arr = [list(map(int, input().split())) for _ in range(N)]

white_cnt = 0  # 0으로 이루어진 종이
blue_cnt = 0  # 1로 이루어진 종이

recur(0, 0, N)

print(white_cnt)
print(blue_cnt)

