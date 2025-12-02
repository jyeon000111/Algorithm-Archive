N, M = map(int, input().split())
num_arr = list(map(int, input().split()))
# 비내림차순, 중복되는 수열을 여러 번 출력하면 안됨.

# 중복 제거한 오름차순 숫자 리스트
num_list = sorted(list(set(num_arr)))
# 각 숫자의 개수 리스트 (인덱스 일치)
cnt_list = [0] * len(num_list)

for num in num_arr:
    num_idx = num_list.index(num)
    cnt_list[num_idx] += 1

result_list = []

def print_sub(start):
    if len(result_list) == M:
        print(*result_list)
        return

    for idx in range(start, len(num_list)):
        if cnt_list[idx] == 0:  # 해당 숫자가 남아 있지 않으면
            continue  # 패스
        # 남아 있으면
        result_list.append(num_list[idx])  # 현재 숫자를 결과 리스트에 담고
        cnt_list[idx] -= 1  # 해당 숫자의 개수 차감

        print_sub(idx)

        # 재귀 후 원상복구
        result_list.pop()
        cnt_list[idx] += 1

print_sub(0)

