# 9 * 9 격자판에서 최댓값을 찾아 출력한다.
# 다음 줄에 몇 행 몇 열에 위치한 수인지도 출력한다.
# [최댓값, 행 번호, 열 번호] 리스트로 묶어 함께 저장한다.
# [-1, 0, 0] 으로 초기화 (모든 값이 0인 엣지케이스 고려)
result_list = [-1, 0, 0]
for row_num in range(1, 10):
    current_row = list(map(int, input().split()))
    for idx, num in enumerate(current_row):
        if num > result_list[0]:
            col_num = idx + 1
            result_list = [num, row_num, col_num]

print(result_list[0])
print(result_list[1], result_list[2])
    