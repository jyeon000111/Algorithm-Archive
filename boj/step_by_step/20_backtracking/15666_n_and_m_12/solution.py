N, M = map(int, input().split())
num_arr = list(map(int, input().split()))
# 같은 수를 여러 번 고를 수 있음 -> 중복 제거 후 사용
# 비내림차순 -> 오름차순 정렬
numbers = sorted(list(set(num_arr)))

result_list = []
def print_sub(start):
    '''탐색 시작할 인덱스를 인자로 받아
    길이 M인 수열을 출력하는
    함수입니다.
    '''
    if len(result_list) == M:
        print(*result_list)
        return

    for idx in range(start, len(numbers)):
        result_list.append(numbers[idx])

        print_sub(idx)
        # 재귀호출 후 원상복구
        result_list.pop()

print_sub(0)
