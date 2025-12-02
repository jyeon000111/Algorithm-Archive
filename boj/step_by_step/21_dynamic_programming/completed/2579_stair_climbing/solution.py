# 목표: 마지막 도착 계단 밟기까지 최대 점수 구하기
# - 계단을 1계단씩 2계단씩 오르고, 연속된 3개의 계단을 밟아선 안 된다.

def dynamic(n):
    '''
    dp 배열에 i번째 계단까지의 최대 점수를 기록.
    n-1번째 계단까지의 최대 점수를 반환하는 함수다.
    '''
    if n == 1:
        return stair_score[0]
    elif n == 2:
        return stair_score[0] + stair_score[1]  # 0번 계단에서 올라오는 방법 뿐
    elif n == 3:
        return stair_score[2] + max(stair_score[0], stair_score[1])   # 0번 계단에서 2계단 올라오는 방법 / 1번 계단에서 1계단 올라오는 방법
    dp = stair_score[:]
    dp[1] += dp[0]  # 0번째 계단에서 1계단 오르기
    dp[2] += max(dp[0], stair_score[1])  # 0번째 계단에서 2계단 오르기
    for i in range(3, n):
        up_2stairs = dp[i - 2]  # 2계단 오르기
        # 1계단 오르기: dp[i] 는 dp[i-3]에서 i-1 계단 밟고 올라온 경우뿐
        up_1stair = stair_score[i - 1] + dp[i - 3]
        dp[i] += max(up_1stair, up_2stairs)
    return dp[n-1]



N = int(input())
stair_score = []
for _ in range(N):
    # N개의 계단에 적힌 점수가 주어짐.
    stair_score.append(int(input()))

print(dynamic(N))