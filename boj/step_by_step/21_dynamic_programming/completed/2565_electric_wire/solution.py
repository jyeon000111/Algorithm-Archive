import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: 전깃줄이 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수

# 구간이 겹치지 않게 하려면 제거해야 하는 수
# - (시작점, 끝점)의 가장 긴 증가 수열 or 감소 수열의 길이 = 교차하지 않고 남길 수 있는 전깃줄 수
# - 오름차순 정렬해서 가장 긴 증가 수열의 길이 구하면 됨!

N = int(input())
wires = []
for _ in range(N):
    s, e = map(int, input().split())
    wires.append((s, e))

wires.sort(key=lambda x: (x[0], x[1]))  # 시작점 기준 오름차순 정렬

dp = [1] * N  # dp[i]는 i번째 전깃줄에서 끝나는 가장 긴 증가수열의 길이
for i in range(1, N):
    # i 이전의 시작점, 끝점이 모두 더 작은 전깃줄 중에 최대 dp 값 + 1
    for k in range(i-1, -1, -1):
        # 같은 점에서 시작하는 전깃줄 없음!
        if wires[i][1] > wires[k][1]:
            dp[i] = max(dp[i], dp[k] + 1)

# 전체 전깃줄 개수에서 남길 수 있는 증가수열 전깃줄 개수를 빼면 답
print(N - max(dp))



