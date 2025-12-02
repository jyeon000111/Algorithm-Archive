# Bottom-up DP 로 풀어보기


N = int(input())

dp = [0] * (N+10)  # 인덱스 i에 i를 1로 만들기 위한 최소 연산 횟수 저장 (인덱스 에러 막기 위해 넉넉하게)

for i in range(2, N+1):
    # 1을 빼는 경우로 초기화
    dp[i] = dp[i-1] + 1

    # 2로 나누는 경우 -> 갱신
    if i % 2 == 0:
        dp[i] = min((dp[i // 2] + 1), dp[i])
    # 3으로 나누는 경우 -> 갱신
    if i % 3 == 0:
        dp[i] = min((dp[i // 3] + 1), dp[i])

print(dp[N])