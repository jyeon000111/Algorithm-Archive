import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: n가지 종류의 동전을 사용해서, 가치의 합이 k원이 되도록 하는 경우의 수 구하기
# - 구성이 같고, 순서만 다른 것은 같은 경우
# - 각 동전은 무한정 사용 가능

# DP
# dp[i] = i원 만드는 경우의 수
# n 종류 동전 오름차순 정렬

n, k = map(int, input().split())
coins = list(set([int(input()) for _ in range(n)]))  # 중복 제거

coins.sort()

dp = [0] * (k+1)   # dp[k] 구하는 것이 목적
dp[0] = 1
# for coin in coins:
#     dp[coin] = 1

for coin in coins:
    for val in range(coin, k+1):
        if val - coin < 0:  # 인덱스 에러 방지
            continue
        dp[val] += dp[val - coin]


# print(dp)

print(dp[k])



