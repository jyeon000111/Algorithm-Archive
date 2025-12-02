import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: 두 수열이 주어졌을 때, 가장 긴 공통 부분 수열의 길이 구하기
# LCS(Longest Common Subsequence) 최장 공통 부분 수열

# 둘 중 더 짧은 것 기준으로 공통 부분 탐색
string_1 = input()
string_2 = input()

if len(string_1) > len(string_2):
    string_1, string_2 = string_2, string_1

len_1 = len(string_1)  # dp 배열의 길이
len_2 = len(string_2)
dp = [0] * len_1  # 공통 부분 수열이 없는 경우 길이 0으로 초기화.
# dp[i]는 string_1의 i번째 문자까지 포함하는 가장 긴 공통 수열의 길이
dp_end_idx = [-1] * len_1  # dp[i]에서 string_2의 수열 끝 위치
for idx in range(len_2):
    if string_2[idx] == string_1[0]:
        dp[0] = 1
        dp_end_idx[0] = idx
        break

for i in range(1, len_1):
    for k in range(i-1, -1, -1):  # 이전 문자 탐색 -> 이전 문자의 끝 위치 이후에 현재 문자 있으면 dp 값 + 1 으로 최댓값 갱신
        print(f'{i}번째 인덱스 string_1의 {string_1[i]}와 이전 문자 {k}번째 인덱스 {string_1[k]}')

        for idx2 in range(dp_end_idx[k] + 1, len_2):
            if string_2[idx2] == string_1[i]:
                if dp[i] < dp[k] + 1:
                    dp[i] = dp[k] + 1
                    dp_end_idx[i] = idx2
                print(f'string_2에서 같은 문자 {string_2[idx2]} 위치 {idx2} 인덱스')
                print(dp)
                break  # for idx2

print(dp)
print(max(dp))