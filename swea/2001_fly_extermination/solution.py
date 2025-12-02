import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# N*N 배열에 M*M 사이즈의 파리채를 내리칠 때, 죽은 파리 수의 최댓값 구하기
# 완전탐색
# - 파리채의 좌상단 기준으로!

def calculte_sum(r, c):
    result = 0  # 잡은 파리 수

    for dr in range(M):
        for dc in range(M):
            nr = r + dr
            nc = c + dc
            # print('현재 좌표', f'({nr}, {nc})')
            result += arr[nr][nc]
    
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 파리채의 크기 M*M
    arr = [list(map(int, input().split())) for _ in range(N)]  # N*N 배열 (숫자는 파리 수)

    max_flies = -1

    for r_idx in range(N - M + 1):  # 파리채 좌상단 기준
        for c_idx in range(N - M + 1):
            cur_flies = calculte_sum(r_idx, c_idx)
            if max_flies < cur_flies:
                max_flies = cur_flies
    
    print(f'#{tc} {max_flies}')


            

