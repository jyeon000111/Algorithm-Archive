# The "What" (최종 코드)

n, m = map(int, input().split())

# 바구니에 처음 들어있는 공의 번호를 리스트로 나열한다.
basket = list(range(1, n+1))

for case in range(m):
    # i번 바구니와 j번 바구니에 들어 있는 공을 교환한다.
    i, j = map(int, input().split())
    # 인덱스로 치면 i-1, j-1 에 해당하는 값을 서로 바꾼다.
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)