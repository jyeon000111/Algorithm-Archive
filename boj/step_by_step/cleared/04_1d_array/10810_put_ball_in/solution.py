# The "What" (최종 코드)

# - 바구니 1~N 번
# - 공 1~N 번까지 존재

n, m = map(int, input().split())

# 바구니 n개에 들어가 있는 공 번호를 나열할 리스트를 모두 0으로 초기화한다.
basket = [0] * n

# 공을 M 번 넣는다
for case in range(m):
    i, j, k = map(int, input().split())
    # i번~j번 바구니까지 k번호의 공을 넣는다.
    # 바구니에 이미 있으면, 기존 공 빼고 새로 넣는다.
    # - 리스트의 인덱스로 치면 i-1 부터 j-1의 값을 k로 재할당한다.
    for index in range(i-1, j):
        basket[index] = k


print(*basket)
