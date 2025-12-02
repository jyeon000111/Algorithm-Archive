n, m = map(int, input().split())
a = []
b = []
for row in range(n):
    a.append(list(map(int, input().split())))
for row in range(n):
    b.append(list(map(int, input().split())))

# 둘을 더한 n행 m열의 2차원 행렬을 0으로 초기화한다.
a_plus_b = [[0]*m for _ in range(n)]
for row_idx in range(n):
    for col_idx in range(m):
        a_plus_b[row_idx][col_idx] = a[row_idx][col_idx] + b[row_idx][col_idx]

for row in a_plus_b:
    print(*row)