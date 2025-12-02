# 목표: 최대로 마실 수 있는 포도주의 양 구하기.
# - 연속 3잔 마실 수 없다. (맨 앞부터 순서대로 마시기)
# - Bottom-Up 점화식으로 DP 배열 채우기


n = int(input())  # 포도주 잔의 개수
# n개 잔에 담긴 포도주 양이 순서대로 주어짐
wine_liter = []  # 0~(n-1) 번 인덱스
for _ in range(n):
    wine_liter.append(int(input()))

dp = wine_liter[:] + ([0] * 10)  # dp[i]는 앞에서부터 인덱스 i번째 잔까지 고려했을 때의 최대량 (인덱스 에러 방지로 넉넉하게)

dp[1] += dp[0]

if n >= 2:
    # 0, 1, 2 연속으로 마실 수 없음 -> 0, 2 / 1, 2 / 0, 1 세 가지 경우의 수
    dp[2] += max(dp[0], wine_liter[1])   # 마시는 경우
    dp[2] = max(dp[1], dp[2])  # 마시지 않는 경우도 고려

for i in range(3, n):
    # i번째 잔을 먹지 않는 경우: dp[i-1]
    # i번째 잔을 먹는 두가지 경우: dp[i-2]에서 1칸 건너뛰고 i잔 먹는 경우 / dp[i-3]에서 1칸 건너뛰고 i-1 먹고 오는 경우
    dp[i] = max(dp[i-1], (wine_liter[i] + dp[i-2]), (wine_liter[i] + dp[i-3] + wine_liter[i-1]))


# 구하는 값: dp 배열을 0~n-1 까지 채웠을 때, dp[n-1]
print(dp[n-1])