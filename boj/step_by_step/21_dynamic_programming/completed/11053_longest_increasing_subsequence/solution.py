import sys
sys.stdin = open("input.txt", "r")

# 목표: 가장 긴 증가하는 부분 수열의 길이 구하기


N = int(input())
num_arr = list(map(int, input().split()))  # 길이 N인 수열

dp = [1] * N  # dp[i] 는 i번째 인덱스 숫자를 포함하는 가장 긴 부분 수열의 길이 (기본적으로 자기자신의 길이 1)

for i in range(N):
    for k in range(i-1, -1, -1):
        if num_arr[k] < num_arr[i]:  # num_arr[i] 이전 수 중 작은 수 최대 dp 값 에 +1
            dp[i] = max((dp[k] + 1, dp[i]))


print(max(dp))



