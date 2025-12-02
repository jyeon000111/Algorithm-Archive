# 목표: 맨 위층에서 아래층 바로 밑 또는 대각선 오른쪽 수를 선택하며 내려올 때, 선택한 수들의 합의 최댓값 구하기

def get_max_sum(n):
    '''
    n 높이의 삼각형을 내려오며 수를 하나씩 선택합니다.
    dp 기법으로 선택한 수들의 최댓값들을 위에서부터 기록하고 반환합니다.
    '''
    dp = [row[:] for row in triangle]  # 삼각형 2차원 배열의 각 자리에 최댓값을 기록
    for i in range(1, n):  # 1행부터 기록
        for j in range(i+1):  # i행은 0 ~ i열까지 존재
            # i행 j열의 최댓값은 왼쪽 대각선 위의 최댓값, 바로 위의 최댓값 중 더 큰 값을 더한 것과 같다.
            if j == 0:  # 맨 왼쪽 값일 때
                dp[i][j] += dp[i-1][j]
            elif j == i:  # 맨 오른쪽 값일 때
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

    return max(dp[n-1])  # 마지막 행의 최댓값


N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]
print(get_max_sum(N))