import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: 배열 B를 오름차순 정렬했을 때, B[k] 구하기
# N*N 배열 A : A[i][j] = i * j
# 1차원 배열 B - N*N 크기


N = int(input())
k = int(input())  # 구하는 값: N*N 배열의 k번째로 작은 수

