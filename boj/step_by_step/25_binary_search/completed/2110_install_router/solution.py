import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------
def install(dist, N):
    '''
    공유기 사이의 간격과 집의 개수를 인자로 받아,
    C개의 공유기를 모두 설치할 수 있는지 확인하고,
    가능하면 True, 불가능하면 False를 반환한다.
    '''
    cnt = 1  # 맨 왼쪽에 하나 설치
    cur_i = 0  # 마지막으로 설치한 위치

    for next_i in range(1, N):
        if houses[next_i] >= houses[cur_i] + dist:
            cnt += 1
            cur_i = next_i

    return cnt >= C


# 목표: C개의 공유기를 N개의 집에 설치할 때, 가장 인접한 두 공유기 사이의 최대 거리 구하기
# => 파라메트릭 서치
N, C = map(int, input().split())  # N은 집의 개수, C는 공유기의 개수
# 집의 좌표들
houses = []

for _ in range(N):
    houses.append(int(input()))

left_house = min(houses)
right_house = max(houses)

houses.sort()

left = 1
right = right_house - left_house

while left <= right:
    mid = (left + right) // 2  # 공유기 사이의 거리

    if install(mid, N):  # 설치 가능하면 거리를 넓힌다.
        left = mid + 1
    else:  # 불가능하면 거리를 좁힌다.
        right = mid - 1

print(right)