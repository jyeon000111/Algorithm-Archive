# 두 수를 역순으로 뒤집고, 그 중 큰 수 출력하기
a, b = input().split()

a_reversed = int(a[::-1])
b_reversed = int(b[::-1])

print(max(a_reversed, b_reversed))



