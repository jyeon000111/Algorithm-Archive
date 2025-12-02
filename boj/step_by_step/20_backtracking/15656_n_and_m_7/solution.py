N, M = map(int, input().split())
num_arr = list(map(int, input().split()))

# N개의 자연수 중 M개를 고른 수열(중복 허용) -> 사전 순 출력
# 숫자 배열 오름차순 정렬
num_arr.sort()
result_arr = []

def subsequence(cnt):
    '''리스트에 담은 숫자의 개수를 인자로 받아
    길이 M인 수열을 출력하는 함수입니다.
    '''
    if cnt == M:
        print(*result_arr)
        return

    for num in num_arr:
        result_arr.append(num)
        subsequence(cnt+1)
        result_arr.pop()

subsequence(0)