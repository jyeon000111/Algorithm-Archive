import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: M미터 이상의 나무를 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값 구하기
# - 설정 높이 이상의 길이를 가져갈 수 있음.

# => Parametric Search

N, M = map(int, input().split())  # N은 나무의 개수, M은 가져가려는 나무의 길이
trees = list(map(int, input().split()))

left = 0
right = max(trees)

while left <= right:
    mid = (left + right) // 2  # 절단기 높이
    cur_length = 0
    for tree in trees:
        if tree > mid:
            cur_length += tree - mid

    # 길이가 충분한 경우 높이를 높인다
    if cur_length >= M:
        left = mid + 1
    # 길이가 부족하면 높이를 낮춘다.
    else:
        right = mid - 1

print(right)
