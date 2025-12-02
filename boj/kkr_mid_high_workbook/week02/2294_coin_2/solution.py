import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: n가지 종류의 동전을 최대한 적게 사용해서 가치의 합이 k원이 되도록 한다. 사용한 동전 개수의 최솟값 출력 (불가능하면 -1)
# - 각 동전 무한정 사용 가능

# DP
# dp[i]: i원을 만드는 동전 수의 최솟값
# dp[0] = 0
# dp[k] 구하기..



n, k = map(int, input().split())
coins = list(set([int(input()) for _ in range(n)]))  # 무한 사용 가능 => 중복 제거

coins.sort(reverse=True)  # 내림차순 정렬: 기본적으로 큰 단위부터 사용해야 동전 수가 적어지므로

dp = [0] * (k+1)
dp[0] = 0
for coin in coins:  # 큰 동전부터 체크
    for val in range(coin, k+1):
        if dp[val] != 0:  # 처음 만드는 금액인 경우에만 갱신 (이미 기록된 값은 이미 최소 개수)
            continue
        if val - coin < 0:  # 인덱스 에러 방지
            continue

        dp[val] = dp[val - coin] + 1
    print('현재 동전 금액:', coin, '/ 현재 DP 배열:', dp)

print([num for num in range(k+1)])
print(dp)
