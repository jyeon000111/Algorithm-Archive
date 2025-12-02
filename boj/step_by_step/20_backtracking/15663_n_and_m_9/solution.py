N, M = map(int, input().split())
# 사전 순 출력, 중복 허용
num_arr = list(map(int, input().split()))
# 숫자를 오름차순으로 리스트에 저장
num_list = sorted(list(set(num_arr)))
# 각 숫자의 개수를 리스트에 저장 (인덱스 일치시키기)
num_cnt_list = [0] * len(num_list)
for num in num_arr:
    num_idx = num_list.index(num)
    num_cnt_list[num_idx] += 1

result_list = []

def print_sub(cnt):
    '''리스트에 담은 숫자의 개수를 인자로 받아
    길이 M인 수열을 출력하는 함수입니다.
    '''
    if len(result_list) == M:
        print(*result_list)
        return

    for idx in range(len((num_list))):
        if num_cnt_list[idx]  == 0:  # 해당 숫자의 개수가 0개면
            continue   # 패스
        result_list.append(num_list[idx])  # 해당 숫자 결과 리스트에 넣고
        num_cnt_list[idx] -= 1  # 해당 숫자 개수 1 차감

        print_sub(cnt + 1)

        # 재귀 호출 후 원상복구
        result_list.pop()
        num_cnt_list[idx] += 1


print_sub(0)