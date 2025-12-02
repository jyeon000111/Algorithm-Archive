N, M = map(int, input().split())
num_arr = list(map(int, input().split()))

# N개의 자연수 중 M개 고른 수열 (중복 허용, 비내림차순)
num_arr.sort()  # 오름차순 정렬
result_arr = []

def print_sub(start):
    '''탐색 시작 인덱스를 인자로 받아
    비내림차순의 길이 M인 수열을 출력하는 함수입니다.
    '''
    if len(result_arr) == M:
        print(*result_arr)
        return

    for idx in range(start, N):
        result_arr.append(num_arr[idx])

        print_sub(idx)

        # 재귀 후 돌아와서 흔적 지우기
        result_arr.pop()

print_sub(0)