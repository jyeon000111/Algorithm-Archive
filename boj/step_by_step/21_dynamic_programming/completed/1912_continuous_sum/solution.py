# 목표: n개의 정수로 주어진 임의의 수열. 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 최댓값 구하기
# (단, 수는 1개 이상 선택) (수열을 이루는 정수는 -1000 부터 1000까지)


def get_max(n, arr):
    dp = [-float('inf')] * n   # i번째 인덱스에서 끝나는 배열의 최댓값 저장
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i-1]+arr[i])
    return max(dp)


N = int(input())
given_arr = list(map(int, input().split()))
print(get_max(N, given_arr))