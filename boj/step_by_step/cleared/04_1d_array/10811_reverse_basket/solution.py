# 1~N까지 번호가 적힌 바구니 N개
# M번 바구니의 순서를 역순으로 만든다.

n, m = map(int, input().split())

basket = list(range(1, n+1))


for case in range(m):
    # 왼쪽에서 i번째 ~ j번째 바구니 순서를 역순으로 바꾼다. (인덱스로 치면 i-1, j-1)
    # 해당 부분을 역순으로 뒤집어서 슬라이스 할당한다.
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]
    
print(*basket)
    
