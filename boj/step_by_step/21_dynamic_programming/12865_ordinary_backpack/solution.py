import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: N 개의 물건들 중에서 최대 K만큼의 무게(W)만 챙길 수 있다. 챙긴 물건들의 가치(V) 총합의 최댓값 구하기.


N, K = map(int, input().split())
items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))


# dp[i]: i 무게만큼 챙겼을 때 최대가치
dp = [0] * (K+1)  # 최대로 k만큼 챙겼을 때까지만 체크

for weight, value in items:
    # for idx in range(K, weight-1, -1):
    #     dp[idx] = max(dp[idx], dp[idx-weight] + value)
    for idx in range(K-weight, -1, -1):
        dp[idx + weight] = max(dp[idx + weight], dp[idx] + value)

# print(dp)
print(max(dp))