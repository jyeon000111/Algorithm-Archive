# a, b, c가 1~20 범위일 때만 계산하면 됨.
# 3차원 리스트로 저장 dq[a][b][c] 순서
# 결과는 무조건 1 이상이므로 0으로 초기화
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]


def recur(a, b, c):
    '''
    1. a, b, c 중 0 이하인 수가 있다면 1 반환
    2. a, b, c 중 20 초과인 수가 있다면 w(20, 20, 20) 반환
    3. a < b < c 면, w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c) 반환
    4. 그 외에는 w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1) 반환
    '''
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return recur(20, 20, 20)   
     
    if dp[a][b][c]:
        return dp[a][b][c]
    
    if a < b and b < c:
        dp[a][b][c] = recur(a, b, c-1) + recur(a, b-1, c-1) - recur(a, b-1, c)
    else:
        dp[a][b][c] = recur(a-1, b, c) + recur(a-1, b-1, c) + recur(a-1, b, c-1) - recur(a-1, b-1, c-1)

    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {recur(a, b, c)}')
    
