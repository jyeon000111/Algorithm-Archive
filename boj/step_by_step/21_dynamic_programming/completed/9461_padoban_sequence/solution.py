# 목표: 파도반 수열 P(N)의 값 구하기. 나선에 있는 정삼각형의 변의 길이
# - 규칙: N >= 6일 때, P(N) = P(N-1) + P(N-5)

def padoban(n):
    dp = [0] * (n+10)  # 수열의 n번째 숫자를 n번 인덱스에 저장 (인덱스 에러 방지 위해 넉넉한 크기로)
    dp[1] = dp[2] = dp[3] = 1
    dp[4] = dp[5] = 2
    if n >= 6:
        for i in range(6, n+1):
            dp[i] = dp[i-1] + dp[i-5]
    return dp[n]


T = int(input())
for _ in range(T):
    N = int(input())

    print(padoban(N))