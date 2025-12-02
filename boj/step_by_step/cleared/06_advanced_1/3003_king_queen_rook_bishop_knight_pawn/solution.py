# 올바른 세트의 개수 구성을 리스트에 담는다.
right_set_list = [1, 1, 2, 2, 2, 8]

# 발견한 피스의 개수 구성을 새로운 리스트에 담는다.
found_piece_list = list(map(int, input().split()))

# 더하거나 뺄 개수를 담을 빈 리스트를 생성한다.
result_list = []

# 인덱스를 기준으로 차감한 값을 새 리스트에 담는다.
for idx in range(6):
    result_list.append(right_set_list[idx] - found_piece_list[idx])

# 결과 리스트를 언패킹하여 출력
print(*result_list)