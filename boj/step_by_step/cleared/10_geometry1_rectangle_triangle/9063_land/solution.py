N = int(input())  # 점의 개수

# 목표: N개의 점을 둘러싸는 최소 크기의 직사각형의 넓이 출력
# 가로 길이 = x 좌표 최댓값 - x 좌표 최솟값
# 세로 길이 = y 좌표 최댓값 - y 좌표 최솟값
max_x = -10001
max_y = -10001
min_x = 10001
min_y = 10001
for _ in range(N):
    x, y = map(int, input().split())
    if max_x < x:
        max_x = x
    if max_y < y:
        max_y = y
    if min_x > x:
        min_x = x
    if min_y > y:
        min_y = y

print(abs(max_x - min_x) * abs(max_y - min_y))