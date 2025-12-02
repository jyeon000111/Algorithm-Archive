import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: 부분 수열 중 가장 긴 바이토닉 수열의 길이 구하기

# 바이토닉 수열: 증가하다가 감소하는 수열 (어떤 수부터 감소할 것인가??)
# dp_increase[i]: i번째 수에서 끝나는 가장 긴 증가하는 수열의 길이
# dp_decrease[i]: i번째 수부터 시작하는 가장 긴 감소하는 수열의 길이

N = int(input())  # 수열의 크기
numbers = list(map(int, input().split()))   # 수열
dp_increase = [1] * N
for i in range(1, N):
    for k in range(i-1, -1, -1):
        if numbers[k] < numbers[i]:
            dp_increase[i] = max(dp_increase[i], dp_increase[k] + 1)

dp_decrease = [1] * N
for j in range(N-2, -1, -1):  # 뒤에서부터 채우기
    for k in range(j+1, N):
        if numbers[k] < numbers[j]:
            dp_decrease[j] = max(dp_decrease[j], dp_decrease[k] + 1)

dp_bitonic = [0] * N
for x in range(N):
    dp_bitonic[x] = dp_increase[x] + dp_decrease[x] - 1

print(max(dp_bitonic))

