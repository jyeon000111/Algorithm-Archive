# 목표: 규칙을 만족하면서 1~N번 집을 RGB로 칠하는 비용의 최솟값 구하기
# 규칙: N번 집의 색은 이웃한 집의 색과 달라야 함.

def dynamic_programming(n):
    '''
    DP 기법으로 n번째 집을 각 색으로 칠하는 최소 비용을 구한 뒤,
    그 중에서 또 최솟값을 구해 반환하는 함수입니다.
    '''
    dp = [[0]*3 for _ in range(n+10)]  # dp[집 번호][색상인덱스] 해당 번호를 각 색으로 칠할 때의 최소비용을 저장.
    dp[1][0] = rgb_cost[1][0]
    dp[1][1] = rgb_cost[1][1]
    dp[1][2] = rgb_cost[1][2]

    for i in range(2, n+1):  # 2~n번째 집 (n 입력값은 2 이상으로 주어짐.)
        # 빨간색으로 칠하는 경우는 이전 집을 초록색으로 칠하는 경우와 파란색으로 칠하는 경우로 나뉨.
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb_cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb_cost[i][1]  
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb_cost[i][2]  
    
    return min(dp[n])  # n번째 집을 세 가지 색으로 칠하는 경우 중 최솟값

    


N = int(input())
rgb_cost = [[0, 0, 0]]  # i 번째 집을 각 집을 빨강, 초록, 파랑으로 칠하는 비용
for _ in range(N):
    rgb_cost.append(list(map(int, input().split())))

print(dynamic_programming(N))