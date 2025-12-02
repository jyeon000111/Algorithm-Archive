n = int(input())
    
def dp_fib(n):
    global dp_cnt
    dp = [-1] * (n+1) 
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp_cnt += 1
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 목표: 재귀호출의 실행 횟수, 동적 프로그래밍의 실행 횟수 출력
dp_cnt = 0
recur_cnt = dp_fib(n)

print(recur_cnt, dp_cnt)