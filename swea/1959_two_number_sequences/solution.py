import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: 
# A 숫자열(N개의 숫자)과 B 숫자열(M개의 숫자)을 밀어서 마주보는 위치를 변경 가능할 때, 
# 마주보는 숫자들의 곱들의 합의 최댓값 구하기

# 완전 탐색

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # A의 숫자 개수, B의 숫자 개수
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))

    # 더 짧은 숫자열의 숫자 개수가 곱하는 기준이 된다.
    if N < M:
        short_arr, long_arr = a_arr, b_arr
        short_len, long_len = N, M
    else:
        short_arr, long_arr = b_arr, a_arr
        short_len, long_len = M, N
    
    max_sum = -float('inf') 

    for start_idx in range(long_len - short_len + 1):  # 긴 숫자열의 시작 인덱스: 0 ~ (long_len - short_len)
        cur_sum = 0
        for k in range(short_len):
            cur_sum += short_arr[k] * long_arr[start_idx + k]
        if max_sum < cur_sum:
            max_sum = cur_sum
    
    print(f'#{tc} {max_sum}')
