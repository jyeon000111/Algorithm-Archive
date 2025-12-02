n = int(input())
# 출력할 너비 : 2*n - 1
# 중간 줄(n번째 줄)에서 얼마나 떨어져 있느냐를 기준으로 별의 개수가 달라진다.
# 줄은 1번째부터 (2*n -1)번째 줄까지 있다.
for row_num in range(1, 2*n):
    # 앞쪽 공백의 개수를 구한다.
    blank_count = abs(n - row_num)
    # 해당 줄의 별의 개수를 구한다. (출력할 너비) - (2 * 앞쪽 공백의 개수) 와 같다.
    star_count = (2*n - 1) - 2 * blank_count
    # 공백 + 별 을 출력한다.
    print(' ' * blank_count + '*' * star_count)