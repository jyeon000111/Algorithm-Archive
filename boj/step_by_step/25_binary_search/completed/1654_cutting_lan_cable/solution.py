import sys
sys.stdin = open("input.txt", "r")

# 목표: N개를 만들 수 있는 랜선의 최대 길이
# Parametric Search: 가능한 해의 범위를 좁혀나가기

K, N = map(int, input().split())  # K는 보유중인 랜선의 개수, N은 필요한 랜선의 개수
# (항상 K <= N)
cables = []  # 보유 중인 랜선의 길이
for _ in range(K):
    cables.append(int(input()))

left = 1
right = max(cables)  # 최대 길이가 해가 될 수 있는 범위 끝


while left <= right:
    cnt = 0
    mid = (left + right) // 2  # mid는 자를 길이

    for cable in cables:
        cnt += cable // mid
    # print(f'왼쪽 오른쪽 {left}, {right} / mid는 {mid} / 조각 수는 {cnt}')
    if cnt < N:  # 조각 수가 부족하면 길이 줄이기
        right = mid - 1
    else:  # 조각 수가 충분하면 길이 줄이기
        left = mid + 1


print(right)



