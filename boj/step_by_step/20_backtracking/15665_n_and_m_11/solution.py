N, M = map(int, input().split())
num_arr = list(map(int, input().split()))
# 같은 수를 여러 번 사용할 수 있음. -> 숫자 배열에서는 중복 제거
# 사전 순으로 증가 -> 오름차순 정렬
numbers = sorted(list(set(num_arr)))

result_list = []
def print_sub(cnt):
    '''결과 리스트에 담은 숫자의 개수를 인자로 받아
    길이 M인 수열을 구해 출력하는 함수입니다.
    '''
    if cnt == M:
        print(*result_list)
        return

    for num in numbers:
        result_list.append(num)

        print_sub(cnt + 1)
        # 재귀 호출 후 원상복구
        result_list.pop()

print_sub(0)
