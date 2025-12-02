N, M = map(int, input().split())
num_arr = list(map(int, input().split()))  # N개의 숫자 배열
# N개의 수 중 M개를 고른 수열 출력(오름차순)
num_arr.sort()   # 숫자 배열을 오름차순 정렬

result_arr = []

def subsequence(start):
    '''탐색 시작 인덱스를 인자로 받아
    오름차순의 수열을 만들어
    출력하는 함수입니다.
    '''
    if len(result_arr) == M:  # 길이가 M이 되면
        print(*result_arr)  # 출력하고 종료
        return

    for idx in range(start, N):
        result_arr.append(num_arr[idx])
        subsequence(idx + 1) # 재귀 호출

        # 되돌아와서 흔적 지우기
        result_arr.pop()

subsequence(0)